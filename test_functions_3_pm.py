from functions_3_pm import is_ascending, word_concat


def test_is_ascending():
    # assert is_ascending(1, 3, 6) == True
    assert is_ascending(1,3,6)  # mivel bbolean a fv. visszatérési értéke is, ezért lehet egyszerűsíteni


def test_is_ascending_second():
    assert is_ascending(1, 10, 20) == True


def test_is_ascending_equal_values():
    # assert is_ascending(1, 1, 1) == False
    assert not is_ascending(1,1,1)  # mivel false-t ad vissza, ha negáljuk, akkor True lesz --> sikeres teszt


def test_is_ascending_descending():
    assert is_ascending(20, 10, 1) == False


def test_is_ascending_equal_desc():
    assert is_ascending(20, 10, 20) == False


def test_word_concat_second_longer():
    assert word_concat("alma","korte") == "almakorte"


def test_word_concat_first_longer():
    assert word_concat("cseresznye","meggy") == "meggycseresznye"