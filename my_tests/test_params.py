import utils
import pytest

@pytest.mark.parametrize("n, expected", [
    (0, True),
    (2, True),
    (5, False),
    (12, True)
], ids = ['zero', 'two','five','twelve'])

def test_is_even_param(n, expected):
    assert utils.is_even(n) == expected

@pytest.mark.parametrize("a, b, expected", [
    pytest.param(10,2,5, id ="10/2=5"),
    pytest.param(8,4,2, id ="8/4=2"),
    pytest.param(5,0,"Делить на ноль нельзя", id ="5/0=error"),
])

def test_safe_divide_param(a,b,expected):
    assert utils.safe_divide(a,b) == expected

users = {"Alice": 30, "Bob": 25}

@pytest.mark.parametrize("name, expected", [
    pytest.param("Alice", 30, id="Alice=30"),
    pytest.param("Bob", 25,id="Bob=25"),
    pytest.param("Eve", KeyError,id="Eve is not in list")
])

def test_get_user_age_param(name, expected):
    if isinstance(expected,type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            utils.get_user_age(users, name)
    else:
        assert utils.get_user_age(users,name) == expected

cases = [
    pytest.param("Alice", 30, id="Alice=30"),
    pytest.param("Bob", 25,id="Bob=25")
]

@pytest.mark.parametrize("name, expected", cases)

def test_get_user_age_success(name, expected):
    assert utils.get_user_age(users,name) == expected

@pytest.mark.parametrize("name", [
    pytest.param("Eve",id="Eve is not in list")
])

def test_get_user_age_fail(name):
    with pytest.raises(KeyError):
        utils.get_user_age(users,name)

@pytest.mark.parametrize("name", ["Charlie"], ids = ['one'])
def test_get_user_age_missing(name):
    with pytest.raises(KeyError):
        utils.get_user_age(users, name)
