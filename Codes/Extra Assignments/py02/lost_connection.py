import math

def time_until_lost_connection(direction_A, direction_B):
    vel = 1/12 #km/min

    degrees_diff = abs(direction_A - direction_B)

    teta = math.radians(degrees_diff)
    travelled_distance = math.sqrt((1225)/(2*(1-math.cos(teta)))) #km #law of cosines

    timeToLoseConnection_rounded = round(travelled_distance / vel, 3)

    return timeToLoseConnection_rounded