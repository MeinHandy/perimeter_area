import math as m
supported_shapes = ["square", "circle", "rectangle", "parallelogram"]


def circle_dimensions():
    invalid = True
    while invalid:
        dimension_provided = input("Are you provided a radius or circumference? \n")
        if dimension_provided == "diameter":
            invalid = False
        elif dimension_provided == "radius":
            invalid = False
            continue
        else:
            print("Error, please choose between 'diameter' or 'radius'.")

    invalid = True
    while invalid:
        try:
            dimension = float(input("What is the {} of the circle? \n".format(dimension_provided)))
            invalid = False
        except ValueError:
            print("Please input a number")
    if dimension_provided == "diameter":
        radius = dimension / 2
    elif dimension_provided == "radius":
        radius = dimension
    area = m.pi * radius ** 2
    circumference = m.pi * (2 * radius)
    print("Circle area: {:.2f}, circle circumference: {:.2f} (2 decimal places)".format(area, circumference))


def square_dimensions():
    invalid = True
    while invalid:
        try:
            side = float(input("What is a side dimension? \n"))
            invalid = False
        except ValueError:
            print("Please input a number")
    area = side ** 2
    perimeter = side * 4
    print("Square area: {:.2f}, Square perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def rectangle_dimensions():
    invalid = True
    while invalid:
        try:
            side0 = float(input("What is the first side dimension? "))
            side1 = float(input("What is the second side dimension? "))
            invalid = False
        except ValueError:
            print("Please input a number")
    area = side0 * side1
    perimeter = side0 * 2 + side1 * 2
    print("Rectangle area: {:.2f}, Rectangle perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def parallelogram_dimensions():
    invalid = True
    while invalid:
        try:
            side0 = float(input("What is the first side dimension? "))
            side1 = float(input("What is the second side dimension? "))
            invalid = False
        except ValueError:
            print("Please input a number")
    area = side0 * side1
    perimeter = side0 * 2 + side1 * 2
    print("parallelogram area: {:.2f}, parallelogram perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


while True:
    shape_request = input("What shape dimensions need solving of the following: {}. Type 'exit' to exit the program. \n".format(supported_shapes))
    if shape_request == "circle":  # if/many elif to take the input and direct the program/user in the right direction
        circle_dimensions()
    elif shape_request == "square":
        square_dimensions()
    elif shape_request == "rectangle":
        rectangle_dimensions()
    elif shape_request == "parallelogram":
        parallelogram_dimensions()
    elif shape_request == "exit":
        exit("Manual program exit")
    else:
        print("Invalid shape")
