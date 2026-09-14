import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"(0|[1-9]\d{0,2})(\.(0|[1-9]\d{0,2})){3}"

    if not re.fullmatch(pattern, ip):
        return False

    numbers = ip.split(".")

    for number in numbers:
        if int(number) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
