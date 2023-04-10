import xlsxwriter
from src.read_countries_keywords_xlsx import read_google_trends_xlsx_files
from src.analyze_categories import compute_each_country_genre_count,  assign_countries_points_in_space, perform_k_means_clustering
from src.category_dictionaries import keyword_to_genre_dictionary


# the following function save_clusters_in_excel_file
def save_clusters_in_excel_file(cluster_to_countries_dict, num_of_clusters):
    # the following line creates a workbook
    workbook = xlsxwriter.Workbook(f'countries_in_{num_of_clusters}_clusters.xlsx')
    # the following line creates a worksheet
    worksheet = workbook.add_worksheet()
    # the following line writes the headers of the excel file
    worksheet.write(0, 0, "Country")
    worksheet.write(0, 1, "Cluster Number")
    # the following line writes the clusters in the excel file
    row_num = 0
    for cluster_num in range(num_of_clusters):
        for country in cluster_to_countries_dict[cluster_num]:
            worksheet.write(row_num + 1, 0, country)
            worksheet.write(row_num + 1, 1, cluster_num)
            row_num += 1
    # the following line closes the workbook
    workbook.close()

#compute the clusters and save them in an excel file
def compute_k_means_clustering_and_save_in_excel_file(num_of_clusters):
    # the following line calls the function to read the xlsx files
    country_trends_dict, country_names = read_google_trends_xlsx_files()
    # the following line calls the function to assign each country a point in space
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict, country_names, keyword_to_genre_dictionary)
    country_to_points_dict = assign_countries_points_in_space(country_to_genre_dict, country_to_num_of_keywords_dict)

    # the following line calls the function to perform the k-means clustering algorithm
    cluster_to_countries_dict = perform_k_means_clustering(country_to_points_dict, num_of_clusters)

    # the following line calls the function to save the results in an excel file
    save_clusters_in_excel_file(cluster_to_countries_dict, num_of_clusters)

# compute_k_means_clustering_and_save_in_excel_file(num_of_clusters = 8)