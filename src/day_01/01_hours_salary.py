hour_cost = int(input("Укажите стоимость часа >>> "))
day_quantity = int(input("Укажите количество дней >>> "))

total = (hour_cost * 8) * day_quantity
final = total - (total * .13)

print(final)
