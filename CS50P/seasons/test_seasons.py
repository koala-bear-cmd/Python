from seasons import convert_to_words


def test_one_year():
    assert convert_to_words(525600) == (
        "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_two_years():
    assert convert_to_words(1051200) == (
        "One million, fifty-one thousand, two hundred minutes"
    )


def test_no_and():
    result = convert_to_words(525600)

    assert " and " not in result.lower()


def test_capital_letter():
    result = convert_to_words(1440)

    assert result == "One thousand, four hundred forty minutes"
