
def find_country(some_list: list, country: str) -> list:
    """This function returns a list with visits to required country"""
    res_list = []
    for visit_data in some_list:
        for city, country_2 in visit_data.values():
            if country_2.lower() == country.lower():
                res_list.append(visit_data)
    return res_list


def kill_doubles(some_dict: dict) -> list:
    """This function allows get list with unique values from dict. list values"""
    temp = set()
    for value in some_dict.values():
        for num in value:
            temp.add(num)
    res = list(temp)
    res.sort()
    return res


def make_range(some_list: list) -> dict:
    """This function returns a dict with data with percent of presence"""
    res_dict = {}
    for row in some_list:
        temp = row.split()
        key = f'длина в {len(temp)} слова'
        res_dict.setdefault(key, 0)
        res_dict[key] += 1
    for key, value in res_dict.items():
        temp = (value / len(some_list)) * 100
        percent = f'{round(temp)} %'
        res_dict[key] = percent
    return res_dict


