km = int(input("type the distance do you want travel: "))

if km <= 200:
    price = km * 0.50
else:
    price = km * 0.45

print(f"the value of the price spent: {price} ")
