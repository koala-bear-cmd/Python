import sys
import inflect

from datetime import date


def main():
    birthday = input("Date of Birth: ")

    try:
        birthday = date.fromisoformat(birthday)
    except ValueError:
        sys.exit(1)

    today = date.today()

    difference = today - birthday
    minutes = difference.days * 24 * 60

    print(convert_to_words(minutes))


def convert_to_words(minutes):
    engine = inflect.engine()

    words = engine.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
