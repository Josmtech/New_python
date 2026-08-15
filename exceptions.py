# finding area using function
def rectangle_area():
    area = length * width
    print(area)
    return area


try:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    rectangle_area()


except ValueError:
    print("You entered an invalid measurement")


