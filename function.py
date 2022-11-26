import requests
import configparser


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


def get_token(class_, key):
    c = configparser.ConfigParser()
    c.read('settings.ini')
    token = c[class_][key]
    return token


class Yandex:
    def __init__(self, token, url='https://cloud-api.yandex.net/v1/disk/resources'):
        self.token = token
        self.url = url

    def _get_headers(self):
        return {'Content_Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, folder_path):
        headers = self._get_headers()
        params = {'path': folder_path}
        response = requests.put(self.url, headers=headers, params=params)
        return response.status_code

    def delete_folder(self, folder_path):
        headers = self._get_headers()
        params = {
            'path': folder_path,
            'permanently': 'true',
            'force_async': 'true'}
        response = requests.delete(self.url, headers=headers, params=params)
        return response.status_code

