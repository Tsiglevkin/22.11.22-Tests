
import pytest
from function import find_country, kill_doubles, make_range
from data import geo_logs, ids, queries, russia, france, india, func_3_res, func_1_fixture


@pytest.mark.parametrize('check_list, country, etalon', func_1_fixture)
def test_find_country(check_list, country, etalon):
    result = find_country(some_list=check_list, country=country)
    assert result == etalon


def test_kill_doubles():
    result = kill_doubles(some_dict=ids)
    standart = [15, 35, 54, 98, 119, 213]
    assert result == standart


def test_make_range():
    result = make_range(some_list=queries)
    standart = func_3_res
    assert result == standart
