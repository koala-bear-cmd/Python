import re
answer = input("Please enter your content: ").strip().casefold()

if answer == "forty-two" or answer == "forty two" or answer == "42":
    print("yes")
else:
    print("no")
