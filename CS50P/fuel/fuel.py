while True:
    try:
        value = input("please enter the number:")
        x,y = value.split("/")
        x = int(x)
        y = int(y)
        if x <= y and y != 0 and 0 <= x <= y and y > 0:
         break
    except (ValueError, ZeroDivisionError):
          pass

result = round((x / y) * 100)
if result <= 1:
       print("E")
elif result >= 99:
       print("F")
else:
    print(f"{result}%")
