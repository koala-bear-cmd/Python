def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check the length of the plate
    if not (2 <= len(s) <= 6):
        return False

    # Check that the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that all characters are letters or numbers
    if not s.isalnum():
        return False

    # Find the first digit, if there is one
    for i in range(len(s)):
        if s[i].isdigit():

            # The first digit cannot be zero
            if s[i] == "0":
                return False

            # After the first digit, all characters must be digits
            if not s[i:].isdigit():
                return False

            break

    return True


main()
