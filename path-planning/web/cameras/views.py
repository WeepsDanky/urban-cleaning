from django.shortcuts import render
from .models import Camera, Depot, Route, Waypoint
import json

def map_view(request):
    cameras = list(Camera.objects.all().values('gps_location', 'trash_amount'))
    depot = list(Depot.objects.all().values('gps_location'))
    
    routes = []
    trash_per_route = []

    for route in Route.objects.all():
        waypoints = list(route.waypoints.all().values('gps_location'))
        routes.append(waypoints)

        trash = 0
        for waypoint in waypoints: # this is terrible, should be part of model
            for camera in cameras:
                if waypoint['gps_location'] == camera['gps_location']:
                    trash += camera['trash_amount']
                    break
        trash_per_route.append(trash)

    #print(json.dumps(routes))

    return render(request, 'cameras/map.html', {'cameras': json.dumps(cameras), 'depot': json.dumps(depot), 'routes': json.dumps(routes), 'trash_per_route': json.dumps(trash_per_route)})
