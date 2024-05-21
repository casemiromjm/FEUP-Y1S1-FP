def total_distance(dist, cities):
    #special conditions
    if len(cities) < 2:
        return 0
    
    #dist is a dict with the distance between certain cities as values and a tuple of that cities as keys
    trips = list(zip(cities, cities[1:])) #this represents the smaller trips that compose the bigger trip

    distance_travelled = 0
    for trip in trips:
        distance_to_sum = dist.get(trip, 0)
        distance_travelled += dist.get(trip, 0)
        if trip not in dist:
            trip_reversed = (trip[1], trip[0])
            distance_to_sum = dist.get(trip_reversed, 0)
            distance_travelled += dist.get(trip_reversed, 0)
        if distance_to_sum == 0:
            return -1
    
    return distance_travelled