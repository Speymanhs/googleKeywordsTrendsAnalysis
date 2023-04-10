import os
import pandas as pd

# the following function is used to read the xlsx file named "democracy_data.xlsx" and return a dictionary containing the data
#the possible score for democracy is a real-number between 1.32 and 9.81. The return dictionary of this function is of the format: "Country": score
def read_democracy_data_xlsx_file():
    # define the directory path containing dataset
    dataset_directory = "datasets/"

    #define a dictionar named country_to_democracy_dictionary
    country_to_democracy_dictionary = {}

    # read the xlsx file
    democracy_df = pd.read_excel(os.path.join(dataset_directory, "democracy_data.xlsx"), header=None)

    # assign the first row as column labels
    democracy_df.columns = democracy_df.iloc[0]

    # remove the first row from the dataframe because it is the column labels
    democracy_df = democracy_df[1:]

    # create a dictionary with the first column as keys and the other columns as values
    country_to_democracy_dictionary = {row[0]: row[4] for row in democracy_df.itertuples(index=False)}

    return country_to_democracy_dictionary


# the following code reads the conflicts_and_war_data.xlsx file and returns a dictionary containing the data
# the return dictionary of this function is of the format: "Country": rank
def read_conflicts_and_war_data_xlsx_file():
    # define the directory path containing dataset
    dataset_directory = "datasets/"

    #define a dictionar named country_to_conflicts_and_war_dictionary
    country_to_conflicts_and_war_dictionary = {}

    # read the xlsx file
    conflicts_and_war_df = pd.read_excel(os.path.join(dataset_directory, "conflicts_and_war_data.xlsx"), header=None)

    # assign the first row as column labels
    conflicts_and_war_df.columns = conflicts_and_war_df.iloc[0]

    # remove the first row from the dataframe because it is the column labels
    conflicts_and_war_df = conflicts_and_war_df[1:]

    # create a dictionary with the first column as keys and the other columns as values
    country_to_conflicts_and_war_dictionary = {row[0]: row[4] for row in conflicts_and_war_df.itertuples(index=False)}

    return country_to_conflicts_and_war_dictionary


#the following function is used to read the xlsx file named "Income_Inequality_data.xlsx" and return a dictionary containing the data
#the countries are ranked based on income inequality. Therefore, this function returns a dictionary of this function in the format: "Country": rank
def read_income_inequality_data_xlsx_file():
    # define the directory path containing dataset
    dataset_directory = "datasets/"

    #define a dictionar named country_to_income_inequality_dictionary
    country_to_income_inequality_dictionary = {}

    # read the xlsx file
    income_inequality_df = pd.read_excel(os.path.join(dataset_directory, "Income_Inequality_data.xlsx"), header=None)

    # assign the first row as column labels
    income_inequality_df.columns = income_inequality_df.iloc[0]

    # remove the first row from the dataframe because it is the column labels
    income_inequality_df = income_inequality_df[1:]

    # create a dictionary with the first column as keys and the other columns as values
    country_to_income_inequality_dictionary = {row[0]: row[3] for row in income_inequality_df.itertuples(index=False)}

    return country_to_income_inequality_dictionary


#the following function is used to read the xlsx file named "unemployment_data.xlsx" and return a dictionary containing the data
#the countries are ranked based on the percentage of unemployment. Therefore, this function returns a dictionary of this function in the format: "Country": rank
def read_unemployment_data_xlsx_file():
    # define the directory path containing dataset
    dataset_directory = "datasets/"

    #define a dictionar named country_to_unemployment_dictionary
    country_to_unemployment_dictionary = {}

    # read the xlsx file
    unemployment_df = pd.read_excel(os.path.join(dataset_directory, "unemployment_data.xlsx"), header=None)

    # assign the first row as column labels
    unemployment_df.columns = unemployment_df.iloc[0]

    # remove the first row from the dataframe because it is the column labels
    unemployment_df = unemployment_df[1:]

    # create a dictionary with the first column as keys and the other columns as values
    country_to_unemployment_dictionary = {row[0]: row[7] for row in unemployment_df.itertuples(index=False)}

    return country_to_unemployment_dictionary


# the following function is used to read the xlsx file named "mandatory_service_data.xlsx" and return a dictionary containing the data
#the situation of mandatory_service in that country. The return dictionary of this function is of the format: "Country": mandatory_service_status
def read_mandatory_service_data_xlsx_file():

    mandatory_srvice_status = {"Yes": 2, "De jure": 1, "Uncertain": 3, "unclear": 1, "Infrequent": 1 ,"No": 0}
    # define the directory path containing dataset
    dataset_directory = "datasets/"

    #define a dictionar named country_to_mandatory_service_dictionary
    country_to_mandatory_service_dictionary = {}

    # read the xlsx file
    mandatory_service_df = pd.read_excel(os.path.join(dataset_directory, "mandatory_service_data.xlsx"), header=None)

    # assign the first row as column labels
    mandatory_service_df.columns = mandatory_service_df.iloc[0]

    # remove the first row from the dataframe because it is the column labels
    mandatory_service_df = mandatory_service_df[1:]

    # create a dictionary with the first column as keys and the other columns as values
    country_to_mandatory_service_dictionary = {row[0]: mandatory_srvice_status[row[1]] for row in mandatory_service_df.itertuples(index=False)}

    return country_to_mandatory_service_dictionary

