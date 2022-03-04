from strings import count_vowels, sever_word, is_palindrom, count_a, delete_space


def test_count_a():
    assert count_a("valami") == 2

def test_count_a_missing():
    assert count_a("elemer") == 0


def test_count_vowels():
    assert count_vowels("eredendo") == 4

def test_sever_word():
    assert sever_word("valami") == "v*a*l*a*m*i"

def test_is_palindrom_yes():
    assert is_palindrom("anna")

def test_is_palindrom_no():
    assert not is_palindrom("megy a görög aludni")

def test_delete_space():
    assert delete_space("valamit irtam") == "valamitirtam"

def test_delete_space_back():
    assert delete_space(" nem tudok mit irni ") == "nemtudokmitirni"