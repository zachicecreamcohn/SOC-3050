import pandas as pd
import argparse
import numpy as np
from utils import haversine

# Set up argument parser
parser = argparse.ArgumentParser(description='Calculate and record the number of bike stations within one mile.')
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

# Function to count stations within 5280 feet
def count_stations_within_mile(health_lat, health_lon):
    mile_in_feet = 5280
    count = 0
    for station_lat, station_lon in station_coords:
        dist = haversine((health_lat, health_lon), (station_lat, station_lon))
        if dist <= mile_in_feet:
            count += 1
            # print(f"Station at ({station_lat}, {station_lon}) is {dist - mile_in_feet:.2f} feet away from the health data entry at ({health_lat}, {health_lon})")
    return count

# Calculate the number of bike stations within 1 mile for each health data entry
for index, row in health_data.iterrows():
    count_nearby_stations = count_stations_within_mile(row['lat'], row['long'])
    health_data.at[index, 'Stations_within_1_mile'] = count_nearby_stations
    print(f"PROGRESS: {(index + 1) / len(health_data) * 100:.2f}%")

# Save the health data with the new column
if args.output_file is None:
    args.output_file = args.health_data + '_stations_within_mile.csv'
health_data.to_csv(args.output_file, index=False)
print(f"Data saved to {args.output_file}")