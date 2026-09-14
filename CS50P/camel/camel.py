camelcase = input ("please enter your camelcase naem: ")

for i in camelcase:
    if i.isupper():
        print("_" + i.lower(), end="", sep="")
    else:
        print(i, end="", sep="")
