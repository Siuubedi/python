prod1 = float(input("Enter price 1:"))
prod2 = float(input("Enter price 2:"))
prod3 = float(input("Enter price 3:"))

totalBill = prod1 + prod2 + prod3
print("Total bill is:", totalBill)

averagePrice = totalBill / 3
print("Average price is:", averagePrice)

superhero = input("Enter superhero name:")
if (superhero[0] == "S" or superhero[0] == "s"):
    print(True)

else:
    print(False)
