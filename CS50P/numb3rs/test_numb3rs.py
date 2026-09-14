from numb3rs import validate


def test_valid_addresses():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("140.247.235.144") is True
    assert validate("0.0.0.0") is True


def test_numbers_out_of_range():
    assert validate("256.255.255.255") is False
    assert validate("64.256.128.1") is False
    assert validate("64.128.256.1") is False
    assert validate("64.128.1.256") is False


def test_invalid_number_of_parts():
    assert validate("8.8.8") is False
    assert validate("1.2.3.4.5") is False


def test_invalid_characters():
    assert validate("cat") is False
    assert validate("1.1.1.11111") is False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") is False


def test_leading_zeros():
    assert validate("000.001.010.100") is False
