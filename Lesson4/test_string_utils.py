import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

# делает первую букву заглавной
@pytest.mark.parametrize("str,result", [("skypro", "Skypro"),("скайпро", "Скайпро"),(("12345", "12345"))])
def test_capitilize(str, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(str)
    assert res == result

# убирает пробел перед словом
@pytest.mark.parametrize("str,result", [(" skypro", "skypro"), (" скайпро", "скайпро"), (" 12345", "12345")])        
def test_trim(str,result):
    stringUtils = StringUtils()
    res = stringUtils.trim(str)
    assert res == result

# проверяет наличие буквы в слове
@pytest.mark.parametrize("str,symbol", [("Skypro", "S"), ("Skypro", "k")])
def test_ontains(str,symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(str, symbol)
    assert res == True

# удаляет буквы в слове
@pytest.mark.parametrize("str,symbol, result",[("Skypro", "p", "Skyro"), ("Skypro", "ro", "Skyp")])
def test_elete_symbol(str,symbol,result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(str, symbol)
    assert res == result

# проверяет с соответствие первой буквы в слове
@pytest.mark.parametrize("str,symbol",[("Skypro", "S")])
def test_starts_with(str, symbol):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(str, symbol)
    assert res == True

# проверяет с соответствие последней буквы в слове
@pytest.mark.parametrize("str,symbol",[("Skypro", "o")])
def test_end_with(str, symbol):
    stringUtils = StringUtils()
    res = stringUtils.end_with(str, symbol)
    assert res == True

# проверяет пустую строку
@pytest.mark.parametrize("str", [(""), ("  ")])
def test_is_empty(str):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(str)
    assert res == True

def test_list_to_string():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["Sky", "Pro", "List"], "-")
    assert res == "Sky-Pro-List"