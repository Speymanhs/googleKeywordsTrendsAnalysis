import os
import csv
import pandas as pd

def read_google_trends_xlsx_files():
    # define the directory path containing datasets subfolders
    dataset_directory = "datasets/"

    # define the directory path containing csv files of google trends by country
    googleTrends_directory = os.path.join(dataset_directory, "GoogleTrendsKeywords/")

    # initialize an empty dictionary to store xlsx contents for each country
    country_trends_dict = {}

    # initialize an empty list to store country names
    country_names = []

    # loop through all the files in the directory
    for file_name in os.listdir(googleTrends_directory):
        # check if file is a csv file
        if file_name.endswith(".xlsx"):
            # adds country name to list
            country_names.append(file_name.split(".")[0])

    # loop through all the names in the country_names list and reads corresponding xsls file
    for country_name in country_names:
        # read the xsls file
        df = pd.read_excel(os.path.join(googleTrends_directory, country_name + ".xlsx"), header=None)
        # add a list of column names
        df.columns = ["keyword", "rate"]
        # store the dataframe in the dictionary
        country_trends_dict[country_name] = df
        country_trends_dict[country_name]["keyword"] = country_trends_dict[country_name]["keyword"].astype(str)
    return country_trends_dict, country_names

def get_unique_keywords(country_trends_dict, country_names):
    # list all unique keywords in all countries
    unique_keywords = []

    # loop through all the countries and find out all unique keywords
    for country_name in country_names:
        # loop through all the keywords in the country
        for keyword in country_trends_dict[country_name]["keyword"]:
            # check if keyword is not in the list
            if keyword not in unique_keywords:
                # add keyword to the list
                unique_keywords.append(keyword)
    return unique_keywords
