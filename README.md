# CUAVs-Coding-Challenge

Challenge Overview:

At Canadian UAVs, we handle large amounts of geospatial data, which is the focus of this challenge. The task involves correlating data from two sensors that detect anomalies. However, the sensors are not highly accurate, resulting in false positives and variations in their location readings. Your challenge is to associate the sensor readings based on their coordinates to identify common signals that may have been detected by both sensors. This correlation increases the likelihood that the signal is a genuine detection rather than a false positive.

Input Data:

The two sensors provide different output formats: one sensor outputs data in CSV format, and the other outputs data in JSON format. Please refer to the sample data for the exact format of each sensor's output. Both sensors assign a unique ID to each reading, but note that different sensors may use the same IDs. The sensor readings include location coordinates in decimal degrees, using the WGS 84 format, representing where the anomaly was detected. The sensors have an accuracy of 100 meters, meaning that the reported location is within 100 meters of the actual anomaly location.

Output:

The output should consist of pairs of IDs, where one ID is from the first sensor, and the second ID is from the second sensor.

# Thought Process & Solution Logic

**Understanding the Problem**
The primary goal of this challenge is to correlate sensor readings from two different sources by matching their coordinates within a 100-meter radius. The difficulty arises from:

- Different data formats – CSV and JSON.
-  Potentially large datasets that require an efficient approach.
- False positives due to sensor inaccuracies.
- Geospatial distance calculations to determine whether two readings refer to the same anomaly.

**Chosen Approach: Grid-Based Partitioning**
To solve this problem efficiently, we use a grid-based partitioning strategy. Instead of comparing every reading with every other reading (O(n × m) complexity), we divide the Earth’s surface into a grid of small cells (~100m x 100m) and only compare readings that fall within the same or neighboring grid cells.

**Step-by-Step Breakdown of the Solution**
Step 1: Data Preprocessing
- Read SensorData1.csv (convert CSV to structured data).
- Read SensorData2.json (parse JSON into structured data).
- Extract ID, latitude, and longitude from both datasets.

Step 2: Grid-Based Partitioning
- Define grid cells based on latitude and longitude.
- Each grid cell represents a 100m x 100m area.
- Assign each sensor reading to a corresponding grid cell.
- Store sensor readings in a dictionary structure, where the key is the grid cell and the value is a list of readings in that cell.

Step 3: Matching Readings
- For each reading in SensorData1, check if there are any readings in the same or neighboring grid cells from SensorData2.
- Use the Haversine formula to calculate the great-circle distance between two coordinate points.
- If the distance between two readings is ≤100 meters, consider them a match and store the pair of (Sensor1_ID, Sensor2_ID).

Step 4: Output the Results
- Convert the matched pairs into a JSON format with Sensor1_ID as the key and Sensor2_ID as the value.
- Save the results in output.json.
