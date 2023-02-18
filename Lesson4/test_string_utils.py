import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

# делает первую букву заглавной
@pytest.mark.parametrize("str,result", [("skypro", "Skypro"),("скайпро", "Скайпро"),(("12345", "12345"))])
def test_capitilize_pozitive(str, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(str)
    assert res == result

@pytest.mark.parametrize("str,result", [("skypro", "skypro"), ("слайпро", "скайпро")])
def test_capitilize_negative(str, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(str)
    with pytest.raises(AssertionError):
        assert res == result

# убирает пробел перед словом
@pytest.mark.parametrize("str,result", [(" skypro", "skypro"), (" скайпро", "скайпро"), (" 12345", "12345")])        
def test_trim_pozitive(str,result):
    stringUtils = StringUtils()
    res = stringUtils.trim(str)
    assert res == result

@pytest.mark.parametrize("str,result", [(" skypro", " skypro"), (" скайпро", " скайпро")])        
def test_trim_negative(str,result):
    stringUtils = StringUtils()
    res = stringUtils.trim(str)
    with pytest.raises(AssertionError):
        assert res == result

# проверяет наличие буквы в слове
@pytest.mark.parametrize("str,symbol", [("Skypro", "S"), ("Skypro", "k")])
def test_ontains_pozitive(str,symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(str, symbol)
    assert res == True

@pytest.mark.parametrize("str,symbol", [("Skypro", "W"), ("Skypro", "x")])
def test_ontains_negative(str,symbol):
    stringUtils = StringUtils()
    res = stringUtils.contains(str, symbol)
    with pytest.raises(AssertionError):
        assert res == True

# удаляет буквы в слове
@pytest.mark.parametrize("str,symbol, result",[("Skypro", "p", "Skyro"), ("Skypro", "ro", "Skyp")])
def test_elete_symbol_pozitive(str,symbol,result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(str, symbol)
    assert res == result

@pytest.mark.parametrize("str,symbol, result",[("Skypro", "p", "Skypro"), ("Skypro", "ro", "Skypro")])
def test_elete_symbol_negative(str,symbol,result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(str, symbol)
    with pytest.raises(AssertionError):
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