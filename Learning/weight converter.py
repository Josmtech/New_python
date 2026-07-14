weight = int(input("What is your weight? "))
unit = input("Enter units of measure of your weight 'k' or 'l' ")

if unit.upper() == "L":
    converted_weight = weight * 0.45
    print(f"Your weight is {converted_weight} kilograms")
elif unit.upper() == "K":
    converted_weight = weight / 0.45
    print(f"Your weight is {converted_weight} pounds")
else:
    print("you entered the wrong unit of measurement")

