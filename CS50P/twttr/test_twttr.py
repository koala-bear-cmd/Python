from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
