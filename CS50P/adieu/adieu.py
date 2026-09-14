import re
import inflect
names =[]
p = inflect.engine()
while True:
    try:
        name = input("please enter the names:")
        names.append(name)
        formatted_names = p.join(names)


    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {formatted_names}")
