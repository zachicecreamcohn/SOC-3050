# This file is used to create a csv file from "500 Cities Local Data" that contains only data for a single city
# Specifically, I want a file of Chicago and a file for Seattle

import pandas as pd
import argparse


# create an argument parser
parser = argparse.ArgumentParser(description='Create a csv file of 500 Cities Local Data for a single city')
parser.add_argument('city', type=str, help='The city for which to create a csv file')
parser.add_argument("input_file", type=str, help='The file containing the 500 Cities Local Data')
# output file is optional. The default will be the city name
parser.add_argument('-o', '--output_file', type=str, help='The name of the output file')
args = parser.parse_args()

df = pd.read_csv(args.input_file)

# filter the data for the city
df_city = df[df['PlaceName'] == args.city]


# save the data to a csv file
if args.output_file:
    df_city.to_csv(args.output_file, index=False)
else:
    df_city.to_csv(args.city + '.csv', index=False)
