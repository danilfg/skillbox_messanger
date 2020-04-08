
def salary(hour_cost: int, day_quantity: int):
    total = (hour_cost * 8) * day_quantity
    final = total - (total * .13)

    return final

a = salary(100, 1)
b = salary(100, 2)

print(a, b)