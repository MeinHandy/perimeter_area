import math as m
supported_shapes = ["square", "circle", "rectangle", "parallelogram"]


def circle_dimensions():
    invalid = True
    while invalid:
        try:
            radius = float(input("What is the radius of circle? "))
            invalid = False
            area = m.pi * radius ** 2
            circumference = m.pi * (2 * radius)
        except ValueError:
            print("Please input a number")
    print("Circle area: {:.2f}, circle circumference: {:.2f} (2 decimal places)".format(area, circumference))


def square_dimensions():
    invalid = True
    while invalid:
        try:
            side = float(input("What is a side dimension? "))
            invalid = False
            area = side ** 2
            perimeter = side * 4
        except ValueError:
            print("Please input a number")
    print("Square area: {:.2f}, Square perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def rectangle_dimensions():
    invalid = True
    while invalid:
        try:
            side0 = float(input("What is the first side dimension? "))
            side1 = float(input("What is the second side dimension? "))
            invalid = False
            area = side0 * side1
            perimeter = side0 * 2 + side1 * 2  # the math shouldn't be in the try/except but will be fixed later cause lazy
        except ValueError:
            print("Please input a number")
    print("Rectangle area: {:.2f}, Rectangle perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def parallelogram_dimensions():
    invalid = True
    while invalid:
        try:
            side0 = float(input("What is the first side dimension? "))
            side1 = float(input("What is the second side dimension? "))
            invalid = False
            area = side0 * side1
            perimeter = side0 * 2 + side1 * 2  # the math shouldn't be in the try/except but will be fixed later cause lazy
        except ValueError:
            print("Please input a number")
    print("parallelogram area: {:.2f}, parallelogram perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


while True:
    shape_request = input("What shape dimensions of the following: {}".format(supported_shapes))
    if shape_request not in supported_shapes:
        print("Invalid shape")
        continue
    elif shape_request == "circle":
        circle_dimensions()
    elif shape_request == "square":
        square_dimensions()
    elif shape_request == "rectangle":
        rectangle_dimensions()
    elif shape_request == "parallelogram":
        parallelogram_dimensions()
