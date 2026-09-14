
groceries = {}
while True:
    try:
     item = input().strip().upper()
     groceries[item] = groceries.get(item, 0) + 1


    except EOFError:
     for item in sorted(groceries):
      print(groceries[item], item)
     break
