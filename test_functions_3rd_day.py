# teszt eset == python függvény
from functions_3rd_day import get_max


def test_get_max():
    # given: bemeneti adatok
    a = 5
    b = 12
    # when
    result = get_max(a,b)

    # then
    assert result == 12  # boolean, a test sikeres ha True-t ad vissza

def test_get_max_when_first_value_is_greater():
    assert get_max(200,5) == 200

def test_get_max_equal_values():
    assert get_max(100,100) == 100