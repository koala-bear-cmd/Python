import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


input_file = sys.argv[1]
output_file = sys.argv[2]


students = []


try:
    file = open(input_file, "r")

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")


reader = csv.DictReader(file)

for row in reader:
    last, first = row["name"].split(", ")

    student = {
        "first": first,
        "last": last,
        "house": row["house"]
    }

    students.append(student)


file.close()


file = open(output_file, "w", newline="")

writer = csv.DictWriter(
    file,
    fieldnames=["first", "last", "house"]
)

writer.writeheader()

for student in students:
    writer.writerow(student)


file.close()
