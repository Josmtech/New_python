length = 10
width = 5

def area_rectangle():
    area = length * width
    print(area)

def area_square(side):
    print(side**2)
    return side**2


area_square(4)
area_rectangle()