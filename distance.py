import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the Haversine distance (in meters) between two geographic points.
    """
    R = 6371000  # Radius of Earth in meters
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c
