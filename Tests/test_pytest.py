import pytest
from function import find_country, kill_doubles, make_range, get_token, Yandex
from data import geo_logs, ids, queries, russia, france, india, func_3_res, func_1_fixture

# token = get_token(class_='Yandex', key='token')
# yandex = Yandex(token=token)  # данный метод не работает, ошибка ключа при использовании функции.
# в main эта функция работает.
yandex = Yandex(token='используй свой токен')


class Test_country:
    @pytest.mark.parametrize('check_list, country, etalon', func_1_fixture)
    def test_find_country(self, check_list, country, etalon):
        result = find_country(some_list=check_list, country=country)
        assert result == etalon

    def test_kill_doubles(self):
        result = kill_doubles(some_dict=ids)
        standart = [15, 35, 54, 98, 119, 213]
        assert result == standart

    def test_make_range(self):
        result = make_range(some_list=queries)
        standart = func_3_res
        assert result == standart


class Test_yandex:
    def test_create_folder(self):
        result = yandex.create_folder(folder_path='test_folder')
        etalon = 201
        assert result == etalon

    def test_delete_folder(self):
        result = yandex.delete_folder(folder_path='test_folder')
        etalon = 202
        assert result == etalon

    def test_wrong_data(self):
        result = yandex.create_folder(folder_path=None)
        etalon = 400
        assert result == etalon

    def test_no_found_folder(self):
        result = yandex.delete_folder(folder_path='unexisted_folder')
        etalon = 404
        assert result == etalon

# def test_get_token(self):
#     result = get_token(class_='test', key='test')
#     etalon = 'test_token'
#     assert result == etalon



