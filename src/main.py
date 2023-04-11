from src.read_countries_keywords_xlsx import unzip_google_trends_keywords_compressed
from src.analyze_clusters import compute_k_means_clustering_with_auxiliary_data, find_countries_ending_up_in_same_clusters
from src.save_clusters_to_xlsx import compute_k_means_clustering_and_save_in_excel_file
from src.save_country_points_to_xlsx import save_country_points_to_xlsx
from src.analyze_similar_countries import compute_similarity_between_countries_in_each_group
from src.analyze_clusters import compute_k_means_clustering


if __name__ == "__main__":
    # the following line checks if there is already a folder named "GoogleTrendsKeywords" in the datasets directory
    # if not, it unzips the GoogleTrendsKeywords.zip file in the datasets directory into a folder of a same name
    unzip_google_trends_keywords_compressed()

    number_of_clusters = int(input("Please enter the number of clusters you want to compute: "))
    similarity_criteria = input("Please enter the similarity criteria you want to use (democracy, unemployment, income_inequality, conflicts_and_war, mandatory_service): ")

    #the following line saves the points that represent each country in an excel file
    save_country_points_to_xlsx()

    #the following line compute the clusters and save them in an excel file. Ideally, the number of clusters should vary between 3 to 8
    compute_k_means_clustering_and_save_in_excel_file(num_of_clusters=number_of_clusters)

    #find countries that end up in the same clusters at least 4 times when chenging num_of_clusters from 3 to 8
    print(find_countries_ending_up_in_same_clusters())

    #the following line compute the clusters and measure the similarity between members of each cluster based on similarity_criteria
    #the possible values to choose for similarity_criteria are: "democracy", "unemployment", "income_inequality", "conflicts_and_war", "mandatory_service"
    compute_k_means_clustering_with_auxiliary_data(num_of_clusters=number_of_clusters, similarity_criteria=similarity_criteria)

    #the following line computes the similarity between countries in each group (in final_analysis_data.xlsx) based on similarity_criteria
    compute_similarity_between_countries_in_each_group(similarity_criteria=similarity_criteria)
