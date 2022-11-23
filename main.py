# Дан список с визитами по городам и странам. Напишите код,
# который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."

from function import find_country, kill_doubles, make_range
from pprint import pprint
from data import geo_logs, ids, queries


if __name__ == '__main__':
    func_1 = find_country(some_list=geo_logs, country='Россия')
    pprint(func_1)
    # pprint(geo_logs)

    # func_2 = kill_doubles(some_dict=ids)
    # print(func_2)
    #
    # func_3 = make_range(some_list=queries)
    # pprint(func_3)


