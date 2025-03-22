import csv
import json
from grid_partition import lat_lon_to_grid
from distance import haversine_distance

# Load Sensor 1 (CSV)
def load_sensor1_data(csv_file):
    sensor1_data = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            sensor_id = int(row[0])
            lat, lon = float(row[1]), float(row[2])
            grid_cell = lat_lon_to_grid(lat, lon)
            if grid_cell not in sensor1_data:
                sensor1_data[grid_cell] = []
            sensor1_data[grid_cell].append((sensor_id, lat, lon))
    return sensor1_data

# Load Sensor 2 (JSON)
def load_sensor2_data(json_file):
    sensor2_data = {}
    with open(json_file, 'r') as file:
        data = json.load(file)
        for entry in data:
            sensor_id = entry["id"]
            lat, lon = entry["latitude"], entry["longitude"]
            grid_cell = lat_lon_to_grid(lat, lon)
            if grid_cell not in sensor2_data:
                sensor2_data[grid_cell] = []
            sensor2_data[grid_cell].append((sensor_id, lat, lon))
    return sensor2_data

# Find Matches
def find_matches(sensor1_data, sensor2_data, max_distance=100):
    matches = {}
    for grid_cell, sensor1_readings in sensor1_data.items():
        # Get neighboring grid cells to check
        neighbors = [
            grid_cell,
            (grid_cell[0] + 1, grid_cell[1]), (grid_cell[0] - 1, grid_cell[1]),  # Up, Down
            (grid_cell[0], grid_cell[1] + 1), (grid_cell[0], grid_cell[1] - 1),  # Right, Left
            (grid_cell[0] + 1, grid_cell[1] + 1), (grid_cell[0] - 1, grid_cell[1] - 1),  # Diagonals
            (grid_cell[0] + 1, grid_cell[1] - 1), (grid_cell[0] - 1, grid_cell[1] + 1)
        ]
        
        for neighbor in neighbors:
            if neighbor in sensor2_data:
                for sensor1_id, lat1, lon1 in sensor1_readings:
                    for sensor2_id, lat2, lon2 in sensor2_data[neighbor]:
                        if haversine_distance(lat1, lon1, lat2, lon2) <= max_distance:
                            matches[sensor1_id] = sensor2_id
    return matches

# Main Execution
if __name__ == "__main__":
    sensor1_data = load_sensor1_data("SensorData1.csv")
    sensor2_data = load_sensor2_data("SensorData2.json")
    matched_ids = find_matches(sensor1_data, sensor2_data)
    
    # Save output
    with open("output.json", "w") as outfile:
        json.dump(matched_ids, outfile, indent=4)
    
    print("Matching complete. Results saved in output.json")
