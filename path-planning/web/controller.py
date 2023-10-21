import random
import numpy as np

import django
from django.conf import settings

import googlemaps
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

gmaps = googlemaps.Client(key="AIzaSyCfITtYa7fMn5WJS__mpqWTu-5mNg4mt14")

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': "C:/Users/titus/OneDrive - Imperial College London/Desktop/UrbanClean/web/db.sqlite3",
        }
    },
    INSTALLED_APPS=[
        "cameras",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles"
    ],
)

django.setup()

from cameras.models import Camera, Depot, Route, Waypoint

def get_driving_time(start_coords, end_coords):
    directions_result = gmaps.directions(
        start_coords,
        end_coords,
        mode="driving",
        departure_time="now"
    )

    if directions_result and 'legs' in directions_result[0]:
        duration = directions_result[0]['legs'][0]['duration_in_traffic']['text']
        return duration

    return None


def trialsetup():

    Camera.objects.all().delete()
    Depot.objects.all().delete()

    d = Depot(gps_location="51.5020423,-0.1405588")
    d.save()

    pilecount = 20
    trashrange = [1, 6]
    latituderange = [51.4856887, 51.5001421]
    longituderange = [-0.1862096,-0.150853]

    for pile in range(pilecount):
        gpsloc = str(random.uniform(latituderange[0], latituderange[1])) + "," + str(random.uniform(longituderange[0], longituderange[1]))
        c = Camera(gps_location=gpsloc, trash_amount=random.randint(trashrange[0], trashrange[1]))
        c.save()

def setDepot(gps):
    Depot.objects.all().delete()
    Depot(gps_location=gpsloc).save()


def addCamera(gps, trash=0):
    Camera(gps_location=gpsloc, trash_amount=random.randint(trashrange[0], trashrange[1])).save()
    return Camera.objects.all().count()

def removeCamera(id):
    Camera.objects.get(id=id).delete()

def setTrash(id, val):
    Camera.objects.get(id=id).gps_location = val

def clearCameras():
    Camera.objects.all().delete()


def generate_distance_matrix():
    trashcount = [{"trash_amount" : 1.0}] + list(Camera.objects.all().values('trash_amount'))
    gps_list = [list(Depot.objects.all().values('gps_location'))[0]] + list(Camera.objects.all().values('gps_location'))

    gps_count = len(gps_list)
    distmat = np.ones((gps_count, gps_count)) * 999999

    for f in range(gps_count):
        for t in range(gps_count):
            if f == t:
                distmat[f][t] = 0

            else:
                time = get_driving_time(gps_list[f]["gps_location"], gps_list[t]["gps_location"])
                print(time)
                if time:
                    if "hours" in time:
                        hsplit = time.split(" hours ")
                        minutecost = int(hsplit[0]) * 60 + int(hsplit[1].split(" mins")[0])
                    elif "hour" in time:
                        hsplit = time.split(" hour ")
                        minutecost = int(hsplit[0]) * 60 + int(hsplit[1].split(" mins")[0])
                    else:
                        minutecost = int(time[0].split(" mins")[0])

                    distancecost = minutecost * 60 # / trashcount[t]["trash_amount"] # make sure this shouldn't be trashcount[f]
                    distmat[f][t] = distancecost
                else:
                    print("Error in calculating time from", gps_list[f]["gps_location"], "to", gps_list[t]["gps_location"])
                    # keep default
    np.save("distcache.npy", distmat)

def optimizeVRP():

    data = {} # list(Camera.objects.all().values('gps_location'))

    data["distance_matrix"] = np.load("distcache.npy")
    print(data["distance_matrix"])
    data["num_vehicles"] = 2
    data["depot"] = 0

    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Distance constraint.
    dimension_name = "Distance"
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name,
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    gps_list = [list(Depot.objects.all().values("gps_location"))[0]] + list(Camera.objects.all().values("gps_location"))

    Route.objects.all().delete()
    #Waypoint.objects.all().delete() should be done automatically

    for i in range(data["num_vehicles"]):
        index = routing.Start(i)
        strbuilder = "Route for vehicle " + str(index) + ":\n"
        r = Route()
        r.save()
        pcount = 0
        while not routing.IsEnd(index):
            gpsl = gps_list[manager.IndexToNode(index)]["gps_location"]

            strbuilder += gpsl + " -> "
            w = Waypoint(route=r, order=pcount, gps_location=gpsl)
            w.save()

            index = solution.Value(routing.NextVar(index))
            pcount += 1

        gpsl = gps_list[manager.IndexToNode(index)]["gps_location"]
        strbuilder += str(format(gpsl))
        w = Waypoint(route=r, order=pcount, gps_location=gpsl)
        w.save()

        print(strbuilder)



#trialsetup()
#generate_distance_matrix()
optimizeVRP()
