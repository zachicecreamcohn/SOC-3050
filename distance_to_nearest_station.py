import pandas as pd
import argparse
import numpy as np
from utils import haversine

# Set up argument parser
parser = argparse.ArgumentParser(description='Calculate and record the distance in feet to the nearest station.')
parser.add_argument('bike_station_data', type=str, help='Path to the bike station data file.')
parser.add_argument('health_data', type=str, help='Path to the health data file.')
parser.add_argument('-o', '--output_file', type=str, help='Path to the output file.', nargs='?')
args = parser.parse_args()

# Read the bike station data
bike_station_data = pd.read_csv(args.bike_station_data)

# Read the health data
health_data = pd.read_csv(args.health_data)

# Precompute station coordinates as tuples
station_coords = [(lat, lon) for lat, lon in zip(bike_station_data['lat'], bike_station_data['long'])]

# Function to find the nearest station
def find_nearest_station(health_lat, health_lon):
    min_distance = float('inf')
    nearest_station = None
    for station_lat, station_lon in station_coords:
        dist = haversine((health_lat, health_lon), (station_lat, station_lon))
        if dist < m in_distance:
            min_distance = dist
            nearest_station = (station_lat, station_lon)
    return min_distance

# Calculate the distance to the nearest station for each health data entry
for index, row in health_data.iterrows():
    nearest_distance = find_nearest_station(row['lat'], row['long'])
    health_data.at[index, 'Distance_to_nearest_station'] = nearest_distance
    print(f"PROGRESS: {(index + 1) / len(health_data) * 100:.2f}%")

# Save the health data with the new column
if args.output_file is None:
    args.output_file = args.health_data + '_with_distance.csv'
health_data.to_csv(args.output_file, index=False)
