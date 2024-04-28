# This file will use the FIPS codes in the bike sharing datasets
# to identify and save health data for the same locations.

import pandas as pd
import argparse

# set up argument parser
parser = argparse.ArgumentParser(description='Keep only relevant information from the health data.')
parser.add_argument('health_data', type=str, help='Path to the health data file.')

# add an argument for any number of bike data files
parser.add_argument('bike_dataA', type=str, help='Path to the first bike data file.')
parser.add_argument('bike_dataB', type=str, help='Path to the second bike data file.')

parser.add_argument('output_file', type=str, help='Path to the output file.', default='health_data.csv')
args = parser.parse_args()

# read the health data
health_data = pd.read_csv(args.health_data)

# read the bike sharing data
bike_data_a = pd.read_csv(args.bike_dataA)
bike_data_b = pd.read_csv(args.bike_dataB)

FIPS_codes = []
for bike_data in [bike_data_a, bike_data_b]:
    FIPS_codes += bike_data['FIPS_code'].tolist()


FIPS_codes = list(set(FIPS_codes))

# for each fips code, keep only the first 11 digits
FIPS_codes = [int(str(int(code))[:11]) for code in FIPS_codes]

#
# # keep only the health data for the FIPS codes in the bike sharing data
health_data = health_data[health_data['LocationName'].isin(FIPS_codes)]

# save the health data
health_data.to_csv(args.output_file, index=False)