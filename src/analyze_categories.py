from sklearn.cluster import KMeans
import xlsxwriter
from src.read_countries_keywords_xlsx import read_google_trends_xlsx_files
from src.category_dictionaries import keyword_to_genre_dictionary
def compute_each_country_genre_count(country_trends_dict, country_names, keyword_to_genre_dictionary):
    country_to_genre_dict = {}
    country_to_num_of_keywords_dict = {}
    # the following code is used to find out the number of keywords belonging to each genre in each country and save it in the country_to_genre_dict
    for country_name in country_names:
        # initialize a variable to store the number of keywords in the country
        keyword_count = 0
        # initialize a dictionary to store the number of times a genre appears in the country
        genre_count_dict = {}
        # loop through all the keywords in the country
        for keyword in country_trends_dict[country_name]["keyword"]:
            # increment the keyword count
            keyword_count += 1
            # check if keyword is in the dictionary
            if keyword in keyword_to_genre_dictionary:
                # get the genre of the keyword
                genre = keyword_to_genre_dictionary[keyword]

                if genre in genre_count_dict:
                    # increment the count of the genre
                    genre_count_dict[genre] += 1
                else:
                    # add the genre to the dictionary
                    genre_count_dict[genre] = 1
        # save the genre count dictionary in the country_to_genre_dict
        country_to_genre_dict[country_name] = genre_count_dict

        # add the number of keywords in the country to the dictionary
        country_to_num_of_keywords_dict[country_name] = keyword_count

    return country_to_genre_dict, country_to_num_of_keywords_dict


# the following function gets a genre and prints the sorted list of countries based on the percentage of keywords belonging to that genre
def get_sorted_list_of_countries_based_on_genre_including_none(genre, country_trends_dict, country_names, keyword_to_genre_dictionary):
    # compute and get the number of keywords belonging to each genre in each country and the total number of keywords in each country
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict,
                                                                                              country_names,
                                                                                              keyword_to_genre_dictionary)
    # initialize an empty list to store the number of keywords belonging to the genre in each country
    genre_count_list = []
    # loop through all the countries
    for country_name in country_to_genre_dict:
        # check if the genre is in the country
        if genre in country_to_genre_dict[country_name]:
            # get the number of keywords belonging to the genre in the country
            genre_count = country_to_genre_dict[country_name][genre]
            # get the number of keywords in the country
            num_of_keywords = country_to_num_of_keywords_dict[country_name]
            # compute the percentage of keywords belonging to the genre in the country
            percentage = genre_count / num_of_keywords * 100
            # add the country name and the percentage to the list
            genre_count_list.append([country_name, percentage])
        else:
            # add the country name and 0 to the list
            genre_count_list.append([country_name, 0])
    # sort the list based on the percentage
    genre_count_list.sort(key=lambda x: x[1], reverse=True)
    # print the list
    print(genre_count_list)


# the following function gets a genre and print the sorted list of countries based on
# the percentage of keyword belonging to that genre excluding the none genre
def get_sorted_list_of_countries_based_on_genre_excluding_none(genre, country_trends_dict, country_names, keyword_to_genre_dictionary):
    # compute and get the number of keywords belonging to each genre in each country and the total number of keywords in each country
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict,
                                                                                              country_names,
                                                                                              keyword_to_genre_dictionary)
    # initialize an empty list to store the number of keywords belonging to the genre in each country
    genre_count_list = []
    # loop through all the countries
    for country_name in country_to_genre_dict:
        # check if the genre is in the country
        if genre in country_to_genre_dict[country_name]:
            # get the number of keywords belonging to the genre in the country
            genre_count = country_to_genre_dict[country_name][genre]
            # get the number of keywords in the country without the none genre
            num_of_keywords = country_to_num_of_keywords_dict[country_name] - country_to_genre_dict[country_name]["None"]

            # compute the percentage of keywords belonging to the genre in the country
            percentage = genre_count / num_of_keywords * 100
            # add the country name and the percentage to the list
            genre_count_list.append([country_name, percentage])
        else:
            # add the country name and 0 to the list
            genre_count_list.append([country_name, 0])
    # sort the list based on the percentage
    genre_count_list.sort(key=lambda x: x[1], reverse=True)
    # print the list
    print(genre_count_list)


# the following line calls the function to get the sorted list of countries based on
# the number of keywords belonging to the genre "Action/Fighting/Horror"
# get_sorted_list_of_countries_based_on_genre_including_none("Action/Fighting/Horror")

# the following line calls the function to get the sorted list of countries based on
# the number of keywords belonging to the genre "Action/Fighting/Horror" excluding the none genre
# get_sorted_list_of_countries_based_on_genre_excluding_none("Action/Fighting/Horror")



#the following code assigns each country a point in space  based on the number of keywords belonging to these genres: "Action/Fighting/Horror", "Adventure" abd "RPG"
def assign_countries_points_in_space(country_to_genre_dict, country_to_num_of_keywords_dict):
    genre_list = ["Action/Fighting/Horror", "Adventure", "RPG", "Simulation", "Strategy", "Sports", "Puzzle", "Platformer", "Casual", "Family", "None"]
    # initialize a dictionary to store the points of each country
    country_to_points_dict = {}
    # loop through all the countries
    for country_name in country_to_genre_dict:
        # initialize a list to store the points of the country
        points_list = []
        # loop through all the genres
        for genre in genre_list:
            # check if the genre is in the country
            if country_to_genre_dict[country_name].get(genre) is None:
                genre_count = 0
            else:
                genre_count = country_to_genre_dict[country_name][genre]

            # get the number of keywords in the country
            num_of_keywords = country_to_num_of_keywords_dict[country_name]
            # compute the percentage of keywords belonging to the genre in the country
            percentage = genre_count / num_of_keywords * 100
            # add the percentage to the list
            points_list.append(percentage)
        # save the list of points in the dictionary
        country_to_points_dict[country_name] = points_list
    return country_to_points_dict


# the following code performs the k-means clustering algorithm
def perform_k_means_clustering(country_to_points_dict, num_of_clusters):
    # initialize a list to store the points of each country
    points_list = []
    # loop through all the countries
    for country_name in country_to_points_dict:
        # get the points of the country
        points = country_to_points_dict[country_name]
        # add the points to the list
        points_list.append(points)
    # initialize the k-means clustering object
    kmeans = KMeans(n_clusters=num_of_clusters, random_state=0).fit(points_list)
    # get the labels of the countries
    labels = kmeans.labels_
    # initialize a dictionary to store the countries in each cluster
    cluster_to_countries_dict = {}
    # loop through all the countries
    for i in range(len(country_to_points_dict)):
        # get the country name
        country_name = list(country_to_points_dict.keys())[i]
        # get the cluster of the country
        cluster = labels[i]
        # check if the cluster is in the dictionary
        if cluster_to_countries_dict.get(cluster) is None:
            # add the country to the dictionary
            cluster_to_countries_dict[cluster] = [country_name]
        else:
            # add the country to the dictionary
            cluster_to_countries_dict[cluster].append(country_name)
    return cluster_to_countries_dict


# the following function shows the most popular genres in each country excluding the "None" genre
def show_most_popular_genres_in_each_country_excluding_none():
    country_trends_dict, country_names = read_google_trends_xlsx_files()
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict,
                                                                                              country_names,
                                                                                              keyword_to_genre_dictionary)
    show_most_popular_genres_in_each_country_excluding_none(country_to_genre_dict, country_to_num_of_keywords_dict)
    genre_pecentage_list_all_countries = {}
    # loop through all the countries
    for country_name in country_to_genre_dict:
        # get the number of keywords in the country
        num_of_keywords = country_to_num_of_keywords_dict[country_name]
        # initialize a list to store the percentage of keywords belonging to each genre
        genre_percentage_list = []
        # loop through all the genres
        for genre in country_to_genre_dict[country_name]:
            # check if the genre is not "None"
            if genre != "None":
                # get the number of keywords belonging to the genre
                genre_count = country_to_genre_dict[country_name][genre]
                # compute the percentage of keywords belonging to the genre
                percentage = genre_count / num_of_keywords * 100
                # add the percentage to the list
                genre_percentage_list.append([genre, percentage])
        # sort the list based on the percentage
        genre_percentage_list.sort(key=lambda x: x[1], reverse=True)

        genre_pecentage_list_all_countries[country_name] = genre_percentage_list
        # category_dict = {"Action/Fighting/Horror": 1, "Adventure": 2, "RPG": 3, "Simulation": 4, "Strategy": 5, "Sports": 6,
        #             "Puzzle": 7, "Platformer": 8, "Casual": 9, "Family": 10}

    # the following code saves the results in an xlsx file
    # # initialize the workbook
    workbook = xlsxwriter.Workbook('favourite_categories_per_country.xlsx')
    # # initialize the worksheet
    worksheet = workbook.add_worksheet()
    # Write the header to xlsx file
    worksheet.write(0, 0, "Country")
    worksheet.write(0, 1, "Category")
    # # initialize the row counter
    row = 1
    # # loop through all the countries
    for country_name in country_to_genre_dict:
        # write the country name in the worksheet
        worksheet.write(row, 0, country_name)
        # write the list in the worksheet
        worksheet.write(row, 1, genre_pecentage_list_all_countries[country_name][0][0])
        # increment the row counter
        row += 1
    # close the workbook
    workbook.close()

