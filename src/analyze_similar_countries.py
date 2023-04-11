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


