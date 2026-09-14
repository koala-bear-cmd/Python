import pytest
from working import convert


def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_twelve():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")


def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
