import os
import csv

# define the directory path containing datasets subfolders
dataset_directory = "Datasets/"

# define the directory path containing csv files of google trends by country
googleTrends_directory = os.path.join(dataset_directory, "GoogleTrendsKeyworkds/")

# initialize an empty dictionary to store csv contents
csv_dict = {}

# loop through all the files in the directory
for file_name in os.listdir(googleTrends_directory):
    # check if file is a csv file
    if file_name.endswith(".xlsx"):
        print(file_name)

        # open the csv file and read its contents
        with open(os.path.join(googleTrends_directory, file_name), "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            # store csv contents in dictionary
            csv_dict[file_name] = [row for row in csv_reader]

# print the dictionary containing csv contents
print(csv_dict)