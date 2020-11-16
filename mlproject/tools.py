from mlproject.distance import haversine
from termcolor import colored

def dist(lon1, lat1, lon2, lat2):

    dist = haversine(float(lon1), float(lat1), float(lon2), float(lat2))
    return dist
