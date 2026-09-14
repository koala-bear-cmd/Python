import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to "
        r"(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)",
        s
    )

    if not match:
        raise ValueError

    start_hour = int(match.group(1))
    start_minute = match.group(2)
    start_period = match.group(3)

    end_hour = int(match.group(4))
    end_minute = match.group(5)
    end_period = match.group(6)

    if start_minute is None:
        start_minute = 0
    else:
        start_minute = int(start_minute)

    if end_minute is None:
        end_minute = 0
    else:
        end_minute = int(end_minute)

    if start_period == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12

    if end_period == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12

    return (
        f"{start_hour:02}:{start_minute:02} "
        f"to {end_hour:02}:{end_minute:02}"
    )


if __name__ == "__main__":
    main()
