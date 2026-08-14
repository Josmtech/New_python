numbers = [1, 2, 2, 3, 3 ,5, 6, 4, 5, 6, 7, 8, 7, 7, 5, 9, 1]

unique_values = []

for number in numbers:
    if number not in unique_values:
        unique_values.append(number)


print(numbers)
print(unique_values)
unique_values.sort()
print(unique_values)
