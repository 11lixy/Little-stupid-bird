age = 12
if age < 4:
	print("免费")
elif age <18:
	print("收费五元钱")
else:
	print("收费10元")

age1 = 20
if age1 < 4:
	price = 0
elif age1 <18:
	price = 5
else:
	price = 10
print("\nYou admission cost is $" + str(price) + ".")

age2 = 65
if age2 < 4:
	price = 0
elif age2 <18:
	price = 5
elif age2 >=65:
	price = 5
else:
	price = 10
print("\nYou admission cost is $" + str(price) + ".")

age3 = 12
if age3 < 4:
	price = 0
elif age3 <18:
	price = 5
elif age3 >=65:
	price = 5
print("\nYou admission cost is $" + str(price) + ".")
