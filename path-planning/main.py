import googlemaps

gmaps = googlemaps.Client(key="Your_GOOGLE_API_KEY")


def get_driving_time(start_coords, end_coords):
    directions_result = gmaps.directions(start_coords,
                                         end_coords,
                                         mode="driving",
                                         departure_time="now")

    if directions_result and 'legs' in directions_result[0]:
        duration = directions_result[0]['legs'][0]['duration_in_traffic']['text']
        return duration

    return None


if __name__ == "__main__":
    start = (53.1262966, -0.1853047)
    end = (51.4981577,-0.1798661)

    for i in range(1):
        time = get_driving_time(start, end)
        if time:
            print(time)

            #print(f"Estimated driving time: {time}")
        else:
            print("Could not get driving time.")
