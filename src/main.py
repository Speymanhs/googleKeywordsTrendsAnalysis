from read_countries_keywords_xlsx import unzip_google_trends_keywords_compressed
from src.analyze_clusters import compute_k_means_clustering_with_auxiliary_data
from src.save_clusters_to_xlsx import compute_k_means_clustering_and_save_in_excel_file
from src.save_country_points_to_xlsx import save_country_points_to_xlsx

if __name__ == "__main__":
    # the following line checks if there is already a folder named "GoogleTrendsKeywords" in the datasets directory
    # if not, it unzips the GoogleTrendsKeywords.zip file in the datasets directory into a folder of a same name
    unzip_google_trends_keywords_compressed()

    #the following line saves the points that represent each country in an excel file
    save_country_points_to_xlsx()

    #the following line compute the clusters and save them in an excel file
    compute_k_means_clustering_and_save_in_excel_file(num_of_clusters=8)

    #the following line compute the clusters and measure the similarity between members of each cluster based on similarity_criteria
    compute_k_means_clustering_with_auxiliary_data(num_of_clusters=6, similarity_criteria="conflicts_and_war")


