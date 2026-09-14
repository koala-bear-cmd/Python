coin = [25, 10, 5]
amount_remain = 50

while amount_remain > 0:
    print("Amount Due:", amount_remain)
    insert = int(input("Insert Coin: "))

    if insert in coin:
        amount_remain = amount_remain - insert

print("Change Owed:", abs(amount_remain))
