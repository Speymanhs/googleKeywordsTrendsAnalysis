from src.category_dictionaries import keyword_to_genre_dictionary, keyword_to_num_of_player_dict
from src.read_countries_keywords_xlsx import read_google_trends_xlsx_files


country_trends_dict, country_names = read_google_trends_xlsx_files()


# the following code is used to find out the most popular genre in each country other than "None" as a percentage and the whole genre count
for country_name in country_names:
    # initialize a dictionary to store the number of times a genre appears in the country
    genre_count_dict = {}
    # loop through all the keywords in the country
    for keyword in country_trends_dict[country_name]["keyword"]:
        # check if keyword is in the dictionary
        if keyword in keyword_to_genre_dictionary:
            # get the genre of the keyword
            genre = keyword_to_genre_dictionary[keyword]
            # check if genre is not "None"
            if genre != "None":
                # check if genre is in the dictionary
                if genre in genre_count_dict:
                    # increment the count of the genre
                    genre_count_dict[genre] += 1
                else:
                    # add the genre to the dictionary
                    genre_count_dict[genre] = 1
    # print the country name and the most popular genre
    print(country_name, max(genre_count_dict, key=genre_count_dict.get), max(genre_count_dict.values())/sum(genre_count_dict.values()), genre_count_dict)

