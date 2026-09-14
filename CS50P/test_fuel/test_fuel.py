import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("2/3") == 67


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"


def test_greater_fraction():
    with pytest.raises(ValueError):
        convert("3/2")


def test_negative_fraction():
    with pytest.raises(ValueError):
        convert("-1/2")

    with pytest.raises(ValueError):
        convert("1/-2")

    with pytest.raises(ValueError):
        convert("-1/-2")


def test_not_integer():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1.5/2")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
