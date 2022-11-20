import math as m
supported_shapes = ["square", "circle", "rectangle", "parallelogram", "triangle"]


def try_except(question):  # a function for try/except statements considering they are so highly used
    invalid = True
    while invalid:
        try:
            answer = float(input(question))
            invalid = False
        except ValueError:
            print("Please input a number")
    return answer  # this is the most useful function ever


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
    dimension = try_except("What is the radius/diameter of the circle? \n")  # try/except for circle dimension
    if dimension_provided == "diameter":
        radius = dimension / 2
    elif dimension_provided == "radius":
        radius = dimension
    area = m.pi * radius ** 2
    circumference = m.pi * (2 * radius)
    print("Circle area: {:.2f}, circle circumference: {:.2f} (2 decimal places)".format(area, circumference))


def square_dimensions():
    side = try_except("What is a side dimension? \n")
    area = side ** 2
    perimeter = side * 4
    print("Square area: {:.2f}, Square perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def rectangle_dimensions():
    side0 = try_except("What is the first side dimension? ")
    side1 = try_except("What is the second side dimension? ")
    area = side0 * side1
    perimeter = side0 * 2 + side1 * 2
    print("Rectangle area: {:.2f}, Rectangle perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def parallelogram_dimensions():
    side0 = try_except("What is the first side dimension? ")
    side1 = try_except("What is the second side dimension? ")
    area = side0 * side1
    perimeter = side0 * 2 + side1 * 2
    print("parallelogram area: {:.2f}, parallelogram perimeter: {:.2f} (2 decimal places)".format(area, perimeter))


def triangle_dimensions():
    sides = []
    side_count = int(try_except("How many sides are provided?\n"))  # try_except returns a float, for loops do not like floats, so it is converted into an integer.
    if side_count > 3:
        print("Triangle cannot have >3 sides, that shape is not a triangle.")
    for i in range(side_count):
        side = try_except("What is the dimension of a side? \n")
        sides.append(side)
    if side_count == 3:
        if sides[0] > sides[1] and sides[2]:  # if/elif identifies the hypotenuse, to adjust calculations to exclude it
            area = sides[1] * sides[2] * 0.5  # formula for area of right-angled triangle
        elif sides[1] > sides[2] and sides[0]:
            area = sides[2] * sides[0] * 0.5
        elif sides[2] > sides[0] and sides[1]:
            area = sides[0] * sides[1] * 0.5
        else:  # because one side isn't longer, this is not a valid triangle
            print("Invalid triangle")
        # perimeter = sides[0] + sides[1] + sides[2]
    elif side_count == 2:  # 2 sides means pythagoras is required
        invalid = True
        while invalid:
            unknown = input("What side is unaccounted for? hypotenuse, opposite or adjacent?")  # this is to adjust pythagoras formula as needed
            if unknown == "hypotenuse":
                hypotenuse = m.sqrt(sides[0] ** 2 + sides[1] ** 2)
                area = sides[0] * sides[1] * 0.5
                sides.append(hypotenuse)
                invalid = False
            elif unknown == "opposite" or "adjacent":  # to know which side is the longest; the hypotenuse
                if sides[0] > sides[1]:
                    hypotenuse = sides[0]  # if sides[0] is larger, it has to be the hypotenuse
                    other = sides[1]
                elif sides[1] > sides[0]:
                    hypotenuse = sides[1]  # if sides[0] is not larger, sides[1] is the hypotenuse; double checks
                    other = sides[0]
                else:
                    print("Error hypotenuse is equal to opposite/adjacent")

                moment = m.sqrt(hypotenuse ** 2 - other ** 2)
                area = moment * other * 0.5  # area of triangle cannot use hypotenuse
                sides.append(moment)
                invalid = False
            else:
                print("Please input 'hypotenuse', 'opposite', 'adjacent'.")
        # area = sides[0] * sides[1] * 0.5  # (1/2) base * height, but really just half the area of a square.
    perimeter = sides[0] + sides[1] + sides[2]
    print("triangle area: {:.2f}, perimeter {:.2f}".format(area, perimeter))


while True:  # loops the program until intentional exit
    shape_request = input("What shape dimensions need solving of the following: {}. Type 'exit' to exit the program. \n".format(supported_shapes)).strip().lower()
    if shape_request == "circle":  # if/many elif to take the input and direct the program/user in the right direction
        circle_dimensions()
    elif shape_request == "square":
        square_dimensions()
    elif shape_request == "rectangle":
        rectangle_dimensions()
    elif shape_request == "parallelogram":
        parallelogram_dimensions()
    elif shape_request == "triangle":
        triangle_dimensions()
    elif shape_request == "exit":
        exit("Manual program exit")
    else:
        print("Invalid shape")
