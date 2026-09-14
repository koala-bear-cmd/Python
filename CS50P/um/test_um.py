from um import count


def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1


def test_um_in_sentence():
    assert count("Hello, um, world") == 1
    assert count("This is, um... CS50.") == 1
    assert count("Um, thanks, um") == 2


def test_um_inside_words():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_without_spaces():
    assert count("um?") == 1
    assert count("(um)") == 1
    assert count("um,um") == 2


def test_no_um():
    assert count("Hello, world") == 0
