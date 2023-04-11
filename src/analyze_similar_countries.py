from src.read_auxiliary_data import read_final_analysis_data_xlsx_file, \
                                    read_mandatory_service_data_xlsx_file, \
                                    read_unemployment_data_xlsx_file, \
                                    read_income_inequality_data_xlsx_file, \
                                    read_conflicts_and_war_data_xlsx_file, \
                                    read_democracy_data_xlsx_file

#the following function reverses a dictionary from the format: key: value to the format: value: key taking into account that values can be the same
def reverse_dict(d):
    """
    Reverses a dictionary where values in the initial dictionary can be the same.
    """
    reversed_dict = {}
    for key, value in d.items():
        if value in reversed_dict:
            reversed_dict[value].append(key)
        else:
            reversed_dict[value] = [key]
    return reversed_dict

def compute_similarity_between_countries_in_each_group(similarity_criteria):
    countries_to_groups_dict = read_final_analysis_data_xlsx_file()
    groups_to_countries_dict = reverse_dict(countries_to_groups_dict)

    #the following lines determine which similarity data we want to use and then calls the function that reads the relevent data
    criteria_dictionary = {"democracy": read_democracy_data_xlsx_file(),
                           "unemployment": read_unemployment_data_xlsx_file(),
                           "income_inequality": read_income_inequality_data_xlsx_file(),
                           "conflicts_and_war": read_conflicts_and_war_data_xlsx_file(),
                           "mandatory_service": read_mandatory_service_data_xlsx_file()
                           }
    country_to_criteria_ranking_dict = criteria_dictionary[similarity_criteria]

        
    #the following lines compute the similarity between countries in each group
    for group in groups_to_countries_dict:
        countries_in_group = groups_to_countries_dict[group]

        countries_in_group_with_value = []
        if similarity_criteria == "conflicts_and_war":
            for country in countries_in_group:
                if country not in country_to_criteria_ranking_dict:
                    countries_in_group_with_value.append(country)
                    country_to_criteria_ranking_dict[country] = 50
                else:
                    countries_in_group_with_value.append(country)
            countries_in_group = countries_in_group_with_value
        else:
            for country in countries_in_group:
                if country in country_to_criteria_ranking_dict:
                    countries_in_group_with_value.append(country)
            countries_in_group = countries_in_group_with_value
        
        criteria_mean = 0
        for country in countries_in_group:
            criteria_mean = criteria_mean + country_to_criteria_ranking_dict[country]
        criteria_mean = criteria_mean / len(countries_in_group)
        print("The mean of the " + similarity_criteria + " ranking for the countries in group " + str(group) + " is: " + str(criteria_mean))
        #the following code computes the distance between each country's criteria_ranking with the mean and lists them in ascending order
        countries_to_distance_from_mean_dict = {}
        for country in countries_in_group:
            countries_to_distance_from_mean_dict[country] = abs(country_to_criteria_ranking_dict[country] - criteria_mean)
        countries_to_distance_from_mean_dict = {k: v for k, v in sorted(countries_to_distance_from_mean_dict.items(), key=lambda item: item[1])}
        print("The countries in group " + str(group) + " are sorted by their distance from the mean of the " + similarity_criteria + " ranking:")
        print(countries_to_distance_from_mean_dict)
        print("")

