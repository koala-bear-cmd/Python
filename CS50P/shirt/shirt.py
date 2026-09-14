import sys
import os

from PIL import Image
from PIL import ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


input_name = sys.argv[1]
output_name = sys.argv[2]

input_extension = os.path.splitext(input_name)[1].lower()
output_extension = os.path.splitext(output_name)[1].lower()

extensions = [".jpg", ".jpeg", ".png"]


if input_extension not in extensions:
    sys.exit("Invalid input")

if output_extension not in extensions:
    sys.exit("Invalid output")

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")


try:
    photo = Image.open(input_name)
    shirt = Image.open("shirt.png")

except FileNotFoundError:
    sys.exit("Input does not exist")


photo = ImageOps.fit(photo, shirt.size)

photo.paste(shirt, shirt)

photo.save(output_name)
