price_of_house = 1000000
name = input("Enter your name: ")
size_of_name = len(name)

has_good_credit = False

if has_good_credit:
    down_payment = price_of_house * 0.1
else:
    down_payment = price_of_house * 0.2

print(down_payment)

if size_of_name < 3:
    print("Must at least be 3 characters")
elif size_of_name > 50:
    print("Too long!")
else:
    print("Name looks good. Welcome")