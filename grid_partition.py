import math

# Constants
EARTH_RADIUS_METERS = 6371000  # Earth's radius in meters
GRID_SIZE_METERS = 100  # Each grid cell represents 100m x 100m

def lat_lon_to_grid(lat, lon):
    """
    Converts latitude and longitude into a grid cell (row, col).
    """
    # Convert lat/lon to meters (approximate using Mercator projection)
    lat_meters = lat * (math.pi * EARTH_RADIUS_METERS) / 180
    lon_meters = lon * (math.pi * EARTH_RADIUS_METERS * math.cos(math.radians(lat))) / 180
    
    # Determine the grid cell
    row = int(lat_meters / GRID_SIZE_METERS)
    col = int(lon_meters / GRID_SIZE_METERS)
    
    return (row, col)
