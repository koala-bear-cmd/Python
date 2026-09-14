import sys
import csv

from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    file = open(sys.argv[1], "r")

except FileNotFoundError:
    sys.exit("File does not exist")


rows = []

reader = csv.reader(file)

for row in reader:
    rows.append(row)

file.close()


print(tabulate(rows, headers="firstrow", tablefmt="grid"))
