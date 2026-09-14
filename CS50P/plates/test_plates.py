from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("HELLO") == True


def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_first_two_characters():
    assert is_valid("50CS") == False
    assert is_valid("C5") == False


def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_number_position():
    assert is_valid("CS50P") == False
    assert is_valid("AAA22A") == False


def test_symbols_and_spaces():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
