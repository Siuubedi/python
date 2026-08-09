def sum(a, b):
    print(a+b)


sum(2, 3)


def calc_vat(price):
    new_price = price + price*0.18
    return new_price

final_price = calc_vat(100)
print(final_price)

