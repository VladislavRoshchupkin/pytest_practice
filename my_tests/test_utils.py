import pytest
import utils
def test_is_even():
    assert utils.is_even(4) is True

def test_is_even_false():
    assert utils.is_even(7) is False

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        utils.divide(1, 0)

def test_list_contains():
    assert [1,2] in [[1,2],2,3]

def test_get_user_age():
    users = {"Alice": 30, "Bob": 25}
    assert utils.get_user_age(users, "Alice") == 30

def test_get_user_age_fail():
    users = {"Alice": 30, "Bob": 25}
    with pytest.raises(KeyError):
        utils.get_user_age(users, "GG")

def test_division():
    assert utils.safe_divide(4,2 ) == 2

def test_division_fail():
    assert utils.safe_divide(1, 0) == "Делить на ноль нельзя"



def test_string_upper():
    assert "hello".upper() == "HELLO", "Строка должна быть в верхнем регистре"
