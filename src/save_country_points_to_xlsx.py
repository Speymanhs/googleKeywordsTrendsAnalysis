from src.read_countries_keywords_xlsx import read_google_trends_xlsx_files
from src.analyze_categories import compute_each_country_genre_count, assign_countries_points_in_space
from src.category_dictionaries import keyword_to_genre_dictionary
import xlsxwriter


#the following function saves the coordinates we assign each country to an excel file.
#these coordinates are based on the percentage of keywords belonging to each genre in each country
def save_country_points_to_xlsx():
    # the following list contains the names of the genres in the order they should be written in the excel file
    genre_list = ["Action/Fighting/Horror", "Adventure", "RPG", "Simulation", "Strategy", "Sports", "Puzzle",
                  "Platformer",
                  "Casual", "Family", "None"]
    # the following line calls the function to read the xlsx files
    country_trends_dict, country_names = read_google_trends_xlsx_files()
    # the following line calls the function to assign each country a point in space
    country_to_genre_dict, country_to_num_of_keywords_dict = compute_each_country_genre_count(country_trends_dict,
                                                                                              country_names,
                                                                                              keyword_to_genre_dictionary)
    print(country_to_genre_dict["Afghanistan"])
    # the following code is used to save the country points to xlsx file
    country_to_points_dict = assign_countries_points_in_space(country_to_genre_dict, country_to_num_of_keywords_dict)
    print(country_to_points_dict["Afghanistan"])
    # create a workbook
    workbook = xlsxwriter.Workbook('keyword_percentage_per_country.xlsx')
    # create a worksheet
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Country")
    # write the genre names in the first row
    for i in range(len(genre_list)):
        worksheet.write(0, i+1, genre_list[i])
    # write the country names in the first column
    for i in range(len(country_names)):
        worksheet.write(i + 1, 0, country_names[i]) # the +1 is to skip the first row
    # write the points in the excel file
    for i in range(len(country_names)):
        for j in range(len(genre_list)):
            worksheet.write(i + 1, j + 1, country_to_points_dict[country_names[i]][j])
    # close the workbook
    workbook.close()

# save_country_points_to_xlsx()



