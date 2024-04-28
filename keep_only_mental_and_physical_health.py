import pandas as pd

# read in the file
filepath = "/Users/zacharycohn/Documents/WashU/Statistics for Sociology/Final Project/Data/Health Data/Processed/NY_PLACES_2023 (2021).csv_with_distance.csv"

# read in the file
health_data = pd.read_csv(filepath)

# remove every row that does not have a "Measure" == one of the options
to_keep = ["Mental health not good for >=14 days among adults aged >=18 years", "Physical health not good for >=14 days among adults aged >=18 years"]
health_data = health_data[health_data["Measure"].isin(to_keep)]

# save the file
health_data.to_csv(filepath.split(".csv")[0] + "_CULLED.csv", index=False)