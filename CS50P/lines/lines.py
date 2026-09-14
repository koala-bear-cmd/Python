import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


try:
    file = open(sys.argv[1], "r")

except FileNotFoundError:
    sys.exit("File does not exist")


count = 0

for line in file:
    line = line.strip()

    if line == "":
        continue

    if line.startswith("#"):
        continue

    count = count + 1


file.close()

print(count)
