numbers = [4, 45, 76, 2, 34, 12, 233, 43, 1]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)