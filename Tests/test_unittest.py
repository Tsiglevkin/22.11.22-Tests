# не получается работа с parameterized - ошибка, что функция во время теста возвр. none.
# текст ошибки 'don't know how to make test from: None'

import unittest
from parameterized import parameterized_class, parameterized
from function import find_country, kill_doubles, make_range
from data import geo_logs, ids, queries, russia, france, india, func_3_res, func_1_fixture


class TestFunc(unittest.TestCase):
    # def test_find_country(self):
    #     result = find_country(some_list=geo_logs, country='россия')
    #     etalon = russia
    #     self.assertEqual(result, etalon)

    def test_kill_doubles(self):
        result = kill_doubles(some_dict=ids)
        standart = [15, 35, 54, 98, 119, 213]
        self.assertEqual(result, standart)

    def test_make_range(self):
        result = make_range(some_list=queries)
        standart = func_3_res
        self.assertEqual(result, standart)

    @parameterized.expand(func_1_fixture)
    def test_find_country_2(self, check_list, country, etalon):
        result = find_country(some_list=check_list, country=country)
        self.assertEqual(result, etalon)
