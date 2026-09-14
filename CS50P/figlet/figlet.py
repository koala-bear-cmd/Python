import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(font_list)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in font_list:
            font = sys.argv[2]
        else:
            sys.exit("Font not found")
    else:
        sys.exit("Invalid command")

else:
    sys.exit("Invalid command")

text = input("Input: ")

figlet.setFont(font=font)
print(figlet.renderText(text))
