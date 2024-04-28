# This file is used to create a csv file from "500 Cities Local Data" that contains only data for a single state (city not explicitly present in the dataset)
# Specifically, I want a file of Chicago (IL) and a file for Seattle (WA)

import pandas as pd
import argparse


# create an argument parser
parser = argparse.ArgumentParser(description='Create a csv file of PLACES data for a single state')
parser.add_argument('state', type=str, help='The state abbreviation for which to create a csv file')
parser.add_argument("input_file", type=str, help='The file containing the PLACES data')
# output file is optional. The default will be the city name
parser.add_argument('-o', '--output_file', type=str, help='The name of the output file')
args = parser.parse_args()

df = pd.read_csv(args.input_file)

chicago_counties = ["Cook"]
newyork_counties = ["Bronx", "Kings", "New York", "Queens", "Richmond"]

# filter the data for the city
df_city = df[df['StateAbbr'] == args.state]

if args.state == 'IL':
    df_city = df_city[df_city['CountyName'].isin(chicago_counties)]
elif args.state == 'NY':
    df_city = df_city[df_city['CountyName'].isin(newyork_counties)]



# save the data to a csv file
if args.output_file:
    df_city.to_csv(args.output_file, index=False)
else:
    df_city.to_csv(args.state + '.csv', index=False)
