from function import find_country, kill_doubles, make_range
from pprint import pprint
from data import geo_logs, ids, queries
from function import Yandex, get_token

token = get_token(class_='Yandex', key='token')
yandex = Yandex(token=token)


if __name__ == '__main__':
    # func_1 = find_country(some_list=geo_logs, country='Россия')
    # pprint(func_1)

    # func_2 = kill_doubles(some_dict=ids)
    # print(func_2)

    # func_3 = make_range(some_list=queries)
    # pprint(func_3)

    # print(yandex.create_folder('test_folder'))
    # print(yandex.delete_folder('test_folder'))
    # print(get_token(class_='test', key='test'))


