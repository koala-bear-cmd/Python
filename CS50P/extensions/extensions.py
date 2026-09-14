expression =input("number: ").strip()

x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if z !=0  and y == "+":
    print(x+z)
elif z !=0  and y == "-":
    print(x-z)
elif z !=0  and y == "/":
    print(x/z)
elif z !=0  and y == "*":
    print(x*z)
