from src.read_countries_keywords_xlsx import read_google_trends_xlsx_files
from src.analyze_categories import compute_each_country_genre_count, assign_countries_points_in_space, perform_k_means_clustering
from src.category_dictionaries import keyword_to_genre_dictionary
from src.read_auxiliary_data import read_democracy_data_xlsx_file, \
    read_unemployment_data_xlsx_file, read_income_inequality_data_xlsx_file, \
    read_conflicts_and_war_data_xlsx_file, read_mandatory_service_data_xlsx_file

#the following function computer k-menans clustering algorithm creating a num_of_clusters clusters given as argument
def compute_k_means_clustering(num_of_clusters):
    # the following line calls the function to read the xlsx files
    country_trends_dict, country_names = read_google_trends_xlsx_files()
    # the following line calls the function to assign each country a point in space
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict, country_names, keyword_to_genre_dictionary)
    country_to_points_dict = assign_countries_points_in_space(country_to_genre_dict, country_to_num_of_keywords_dict)
    # the following line calls the function to perform the k-means clustering algorithm
    cluster_to_countries_dict = perform_k_means_clustering(country_to_points_dict, num_of_clusters)
    return cluster_to_countries_dict


# the following function computes similarity between countries in each cluster based on the chosen auxiliary data
def compute_similarity_between_countries_in_each_cluster(cluster_to_countries_dict, num_of_clusters, similarity_criteria, country_to_criteria_ranking_dict):

    # the following goes over all the clusters, computes the mean of the value of the criteria for each country in the cluster and examines the difference between the mean and the value of the criteria for each country in the cluster
    for cluster_num in range(num_of_clusters):
        # the following line gets the list of countries in the cluster
        countries_in_cluster = cluster_to_countries_dict[cluster_num]
        #the following code checks which countries have corresponding value present in the country_to_criteria_ranking_dict and discards the countries that do not have a value from the continuation of the analysis
        countries_in_cluster_with_value = []
        if similarity_criteria == "conflicts_and_war":
            for country in countries_in_cluster:
                if country not in country_to_criteria_ranking_dict:
                    countries_in_cluster_with_value.append(country)
                    country_to_criteria_ranking_dict[country] = 50
                else:
                    countries_in_cluster_with_value.append(country)
            countries_in_cluster = countries_in_cluster_with_value
        else:
            for country in countries_in_cluster:
                if country in country_to_criteria_ranking_dict:
                    countries_in_cluster_with_value.append(country)
            countries_in_cluster = countries_in_cluster_with_value

        # the following line gets the value of the criteria for each country in the cluster
        countries_criteria_values = [country_to_criteria_ranking_dict[country] for country in countries_in_cluster]
        # the following line computes the mean of the value of the criteria for each country in the cluster
        mean_criteria_value = sum(countries_criteria_values)/len(countries_criteria_values)
        # the following line computes the difference between the mean and the value of the criteria for each country in the cluster
        countries_criteria_values_difference_from_mean = [abs(mean_criteria_value - country_criteria_value) for country_criteria_value in countries_criteria_values]
        # the following line prints the results
        print("Cluster number " + str(cluster_num) + " has the following countries: " + str(countries_in_cluster))
        print("The mean value of the criteria for the countries in the cluster is: " + str(mean_criteria_value))
        print("The difference between the mean and the value of the criteria for each country in the cluster is: " + str(countries_criteria_values_difference_from_mean))
        print("The countries that are the most similar to the other countries in the cluster are: ")
        # the following line prints the 5 countries that are the most similar to the mean of the mean_criteria_value of the cluster
        countries_to_difference_from_mean_dict = {}
        for country, difference_from_mean in zip(countries_in_cluster, countries_criteria_values_difference_from_mean):
            countries_to_difference_from_mean_dict[country] = difference_from_mean
        sorted_countries_to_difference_from_mean_dict = sorted(countries_to_difference_from_mean_dict.items(), key=lambda x: x[1])
        print("The countries that are most similar to criteria_mean of the cluster are: ")
        for i in range(10):
            print(sorted_countries_to_difference_from_mean_dict[i][0],  " : ", sorted_countries_to_difference_from_mean_dict[i][1])
        print("The countries that are the most different from the criteria_mean of the cluster are: ")
        # the following line prints the 5 countries that are the most different from the mean of the mean_criteria_value of the cluster
        for i in range(10):
            print(sorted_countries_to_difference_from_mean_dict[-i-1][0], " : ", sorted_countries_to_difference_from_mean_dict[-i-1][1])

        print("")

# the following function gets as argument a num_of_clusters as well as the chosen auxiliary data.
# then it computes the k-means clustering algorithm using num_of_clusters clusters provided as argument,
# and it checks how much the countries in each cluster are similar to each other based on the chosen auxiliary data
def compute_k_means_clustering_with_auxiliary_data(num_of_clusters, similarity_criteria):
    criteria_dictionary = {"democracy": read_democracy_data_xlsx_file(),
                            "unemployment": read_unemployment_data_xlsx_file(),
                            "income_inequality": read_income_inequality_data_xlsx_file(),
                            "conflicts_and_war": read_conflicts_and_war_data_xlsx_file(),
                            "mandatory_service": read_mandatory_service_data_xlsx_file()
                            }
    country_to_criteria_ranking_dict = criteria_dictionary[similarity_criteria]

    # the following line calls the function to read the xlsx files
    country_trends_dict, country_names = read_google_trends_xlsx_files()
    # the following line calls the function to assign each country a point in space
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict, country_names, keyword_to_genre_dictionary)
    country_to_points_dict = assign_countries_points_in_space(country_to_genre_dict, country_to_num_of_keywords_dict)

    # the following line calls the function to perform the k-means clustering algorithm
    cluster_to_countries_dict = perform_k_means_clustering(country_to_points_dict, num_of_clusters)

    # the following line calls the function to compute the similarity between countries in each cluster
    compute_similarity_between_countries_in_each_cluster(cluster_to_countries_dict, num_of_clusters, similarity_criteria, country_to_criteria_ranking_dict)


compute_k_means_clustering_with_auxiliary_data(num_of_clusters = 6, similarity_criteria = "conflicts_and_war")