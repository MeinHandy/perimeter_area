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
    method = int(try_except("How many dimension(s) are known?"))
    if method == 3:  # no advanced triangle calculations needed
        hypotenuse = float(try_except("What is the dimension of the hypotenuse?"))
        side_a = float(try_except("What is the dimension of side A?"))
        side_b = float(try_except("What is the dimension of side B?"))
        area = 0.5 * side_b * side_a
        perimeter = hypotenuse + side_b + side_a
        print("perimeter", perimeter, ". area", area)
    elif method == 2:  # pythagoras required
        invalid = True
        while invalid:
            unknown = input("What dimension is UNKNOWN? (hypotenuse/side A/side B)").lower()
            if unknown == "hypotenuse":
                side_a = float(try_except("What is the dimension of side A?"))
                side_b = float(try_except("What is the dimension of side B"))
                hypotenuse = m.sqrt(side_a ** 2 + side_b ** 2)
                print("Hypotenuse = {}".format(hypotenuse))
                invalid = False
            elif unknown == "side a" or unknown == "side b":
                hypotenuse = float(try_except("What is the dimension of the hypotenuse?"))
                side_a = float(try_except("What is the dimension of side A?"))
                side_b = m.sqrt(hypotenuse ** 2 - side_a ** 2)
                print("Unknown side = {}".format(side_b))
                invalid = False
            else:
                print("Error, please input hypotenuse/side A/side B")
        area = 0.5 * side_a * side_b
        perimeter = hypotenuse + side_b + side_a
        print("perimeter", perimeter, ". area", area)

    elif method == 1:  # requires use of SOHCAHTOA rules
        angle = float(try_except("What is the angle given? (degrees)"))
        known = input("Which side is known? (hypotenuse/opposite/adjacent)")
        if known == "adjacent":
            adjacent = float(try_except("What is the dimension of the adjacent?"))
            opposite = adjacent * m.tan(m.radians(angle))
            hypotenuse = m.sqrt(opposite ** 2 + adjacent ** 2)  # 2 sides are known, pythagoras to find last
            area = 0.5 * adjacent * opposite
            perimeter = adjacent + opposite + hypotenuse
            print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
        elif known == "opposite":
            opposite = float(try_except("What is the dimension of the opposite?"))
            hypotenuse = opposite / m.sin(m.radians(angle))  # calculates hyp
            adjacent = m.sqrt(hypotenuse ** 2 - opposite ** 2)  # calculates adj using hyp and opp using pythagoras
            area = 0.5 * adjacent * opposite
            perimeter = adjacent + opposite + hypotenuse
            print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
        elif known == "hypotenuse":
            hypotenuse = float(try_except("What is the dimension of the hypotenuse?"))
            opposite = hypotenuse * m.sin(m.radians(angle))
            adjacent = m.sqrt(hypotenuse ** 2 - opposite ** 2)  # calculates adj using hyp and opp using pythagoras
            area = 0.5 * adjacent * opposite
            perimeter = adjacent + opposite + hypotenuse
            print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
        else:
            print("error")

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
