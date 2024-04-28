import pandas as pd
import argparse
import re

# Set up argument parser
parser = argparse.ArgumentParser(description='Clean the health data locations.')
parser.add_argument('health_data', type=str, help='Path to the health data file.')
parser.add_argument('output_file', type=str, help='Path to the output file.', nargs='?')
args = parser.parse_args()

# Read the health data
health_data = pd.read_csv(args.health_data)

# Define regex patterns for both coordinate formats
regex_parentheses = r'\(([^,]+),\s*([^)]+)\)'  # Matches '(lat, long)'
regex_point = r'POINT\s*\(\s*([^\s]+)\s+([^\s]+)\)'  # Matches 'POINT (long lat)'

# Function to apply correct regex based on content of the column
def extract_coordinates(row):
    if "POINT" not in row:
        match = re.search(regex_parentheses, row)
    else:
        match = re.search(regex_point, row)
    if match:
        # Check format to determine correct latitude and longitude order
        if 'POINT' in row:
            # For 'POINT (long lat)' format, swap the order
            return pd.Series([float(match.group(2)), float(match.group(1))])
        else:
            # For '(lat, long)' format
            return pd.Series([float(match.group(1)), float(match.group(2))])
    return pd.Series([None, None])

# Assuming the column containing the coordinates is named "Coordinates"
# list the columns and use input() to ask the user to choose which one is the coordinates column
print("The columns in the dataset are:")
for col in health_data.columns:
    print(f"{health_data.columns.get_loc(col)}: {col}")

# Ask the user to choose the column containing the coordinates
coordinates_col_index = int(input("Enter the index of the column containing the coordinates: "))
# use the index to get the column name
coordinates_col = health_data.columns[coordinates_col_index]

health_data[['lat', 'long']] = health_data[coordinates_col].apply(extract_coordinates)
# drop the original coordinates column
health_data.drop(columns=[coordinates_col], inplace=True)

# Save the health data with the new columns
if not args.output_file:
    args.output_file = args.health_data
health_data.to_csv(args.output_file, index=False)
print(f"Cleaned data saved to {args.output_file}")