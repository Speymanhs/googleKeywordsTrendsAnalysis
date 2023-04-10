from src.read_countries_keywords_xlsx import read_google_trends_xlsx_files
from src.analyze_categories import compute_each_country_genre_count, assign_countries_points_in_space, perform_k_means_clustering
from src.category_dictionaries import keyword_to_genre_dictionary




country_trends_dict, country_names = read_google_trends_xlsx_files()
# the following line calls the function to assign each country a point in space
country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict, country_names, keyword_to_genre_dictionary)
country_to_points_dict = assign_countries_points_in_space(country_to_genre_dict, country_to_num_of_keywords_dict)
print(country_to_genre_dict["United Kingdom"])
print(country_to_points_dict["United Kingdom"])
print(country_to_points_dict["Canada"])
print(country_to_points_dict["Australia"])
print(country_to_points_dict["Iran"])


# the following line calls the function to perform the k-means clustering algorithm
cluster_to_countries_dict = perform_k_means_clustering(country_to_points_dict, 5)
print(cluster_to_countries_dict[0])
print(cluster_to_countries_dict[1])
print(cluster_to_countries_dict[3])

