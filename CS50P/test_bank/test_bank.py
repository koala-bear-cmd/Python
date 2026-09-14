from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello, world") == 0


def test_starts_with_h():
    assert value("hi") == 20
    assert value("How are you?") == 20
    assert value("hey") == 20


def test_other_greetings():
    assert value("good morning") == 100
    assert value("What's up?") == 100
    assert value("welcome") == 100


def test_spaces():
    assert value("   hello") == 0
    assert value("   hi") == 20
    assert value("   good morning") == 100
