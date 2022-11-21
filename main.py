import math as m
import pandas as pd
supported_shapes = ["square", "circle", "rectangle", "parallelogram", "triangle"]
dictionary = {"Shape": [], "Area": [], "Perimeter": []}


def try_except(question):  # a function for try/except statements considering they are so highly used
    invalid = True
    while invalid:
        try:
            answer = float(input(question))
            invalid = False
        except ValueError:
            print("Please input a number")
    return answer  # this is the most useful function ever


def circle_dimensions(dictionary):
    invalid = True
    while invalid:
        dimension_provided = input("Are you provided a radius or diameter? \n")
        if dimension_provided == "diameter":
            invalid = False
        elif dimension_provided == "radius":
            invalid = False
        else:
            print("Error, please choose between 'diameter' or 'radius'.")
    dimension = try_except("What is the radius/diameter of the circle? \n")  # try/except for circle dimension
    if dimension_provided == "diameter":  # if/elif to ensure the dimension calculations are using radius
        radius = dimension / 2
    elif dimension_provided == "radius":
        radius = dimension
    else:
        print("An unknown error occurred.")
    area = m.pi * radius ** 2
    circumference = m.pi * (2 * radius)
    print("Circle area: {:.2f}, circle circumference: {:.2f} (2 decimal places)".format(area, circumference))
    dictionary["Area"].append(area)
    dictionary["Perimeter"].append(circumference)


def square_dimensions(dictionary):
    side = try_except("What is a side dimension? \n")  # all square sides are equal
    area = side ** 2
    perimeter = side * 4
    print("Square area: {:.2f}, Square perimeter: {:.2f} (2 decimal places)".format(area, perimeter))
    dictionary["Area"].append(area)
    dictionary["Perimeter"].append(perimeter)

def rectangle_dimensions(dictionary):
    side0 = try_except("What is the first side dimension?\n")
    side1 = try_except("What is the second side dimension?\n")  # the difference in length size is irrelevant in this context
    area = side0 * side1
    perimeter = side0 * 2 + side1 * 2
    print("Rectangle area: {:.2f}, Rectangle perimeter: {:.2f} (2 decimal places)".format(area, perimeter))
    dictionary["Area"].append(area)
    dictionary["Perimeter"].append(perimeter)

def parallelogram_dimensions(dictionary):  # parallelogram is just a rectangle with attitude
    side0 = try_except("What is the first side dimension?\n")
    side1 = try_except("What is the second side dimension?\n")  # the difference in length size is irrelevant in this context
    area = side0 * side1
    perimeter = side0 * 2 + side1 * 2
    print("parallelogram area: {:.2f}, parallelogram perimeter: {:.2f} (2 decimal places)".format(area, perimeter))
    dictionary["Area"].append(area)
    dictionary["Perimeter"].append(perimeter)

def triangle_dimensions(dictionary):
    method = int(try_except("How many dimension(s) are known?\n"))
    if method == 3:  # no advanced triangle calculations needed
        hypotenuse = float(try_except("What is the dimension of the hypotenuse?\n"))  # hypotenuse is unique and must be identified specifically
        side_a = float(try_except("What is the dimension of side A?\n"))  # side_a and side_b are interchangeable in the current context
        side_b = float(try_except("What is the dimension of side B?\n"))
        area = 0.5 * side_b * side_a
        perimeter = hypotenuse + side_b + side_a
        print("perimeter", perimeter, ". area", area)
        dictionary["Area"].append(area)
        dictionary["Perimeter"].append(perimeter)
    elif method == 2:  # pythagoras required
        invalid = True
        while invalid:
            unknown = input("What dimension is UNKNOWN? (hypotenuse/side A/side B)\n").lower()
            if unknown == "hypotenuse":
                side_a = float(try_except("What is the dimension of side A?\n"))
                side_b = float(try_except("What is the dimension of side B\n"))
                hypotenuse = m.sqrt(side_a ** 2 + side_b ** 2)  # calculating hypotenuse with side_a and side_b using pythagoras
                print("Hypotenuse = {}".format(hypotenuse))
                invalid = False
            elif unknown == "side a" or unknown == "side b":
                hypotenuse = float(try_except("What is the dimension of the hypotenuse?\n"))
                side_a = float(try_except("What is the dimension of side A?\n"))
                side_b = m.sqrt(hypotenuse ** 2 - side_a ** 2)
                print("Unknown side = {}".format(side_b))
                invalid = False
            else:
                print("Error, please input hypotenuse/side A/side B")
        area = 0.5 * side_a * side_b
        perimeter = hypotenuse + side_b + side_a
        print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
        dictionary["Area"].append(area)
        dictionary["Perimeter"].append(perimeter)

    elif method == 1:  # requires use of SOHCAHTOA rules and/or pythagoras
        angle = float(try_except("What is the angle given? (degrees)\n"))
        known = input("Which side is known? (hypotenuse/opposite/adjacent)\n")
        if known == "adjacent":
            adjacent = float(try_except("What is the dimension of the adjacent?\n"))
            opposite = adjacent * m.tan(m.radians(angle))
            print("The opposite is {}.".format(opposite))
            hypotenuse = m.sqrt(opposite ** 2 + adjacent ** 2)  # 2 sides are known, pythagoras to find last
            print("The hypotenuse is {}.".format(hypotenuse))
            area = 0.5 * adjacent * opposite
            perimeter = adjacent + opposite + hypotenuse
            print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
            dictionary["Area"].append(area)
            dictionary["Perimeter"].append(perimeter)
        elif known == "opposite":
            opposite = float(try_except("What is the dimension of the opposite?\n"))
            hypotenuse = opposite / m.sin(m.radians(angle))  # calculates hyp
            print("The hypotenuse is {}.".format(hypotenuse))
            adjacent = m.sqrt(hypotenuse ** 2 - opposite ** 2)  # calculates adj using hyp and opp using pythagoras
            print("The adjacent is {}.".format(adjacent))
            area = 0.5 * adjacent * opposite
            perimeter = adjacent + opposite + hypotenuse
            print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
            dictionary["Area"].append(area)
            dictionary["Perimeter"].append(perimeter)
        elif known == "hypotenuse":
            hypotenuse = float(try_except("What is the dimension of the hypotenuse?\n"))
            opposite = hypotenuse * m.sin(m.radians(angle))
            print("The opposite is {}.".format(opposite))
            adjacent = m.sqrt(hypotenuse ** 2 - opposite ** 2)  # calculates adj using hyp and opp using pythagoras
            print("The adjacent is {}.".format(adjacent))
            area = 0.5 * adjacent * opposite
            perimeter = adjacent + opposite + hypotenuse
            print("Area is {:.2f}, perimeter is {:.2f}".format(area, perimeter))
            dictionary["Area"].append(area)
            dictionary["Perimeter"].append(perimeter)
        else:
            print("error")


while True:  # loops the program until intentional exit
    shape_request = input("What shape dimensions need solving of the following: {}. Type 'exit' to exit the program. \n".format(supported_shapes)).strip().lower()
    if shape_request == "circle":  # if/many elif to take the input and direct the program/user in the right direction
        dictionary["Shape"].append(shape_request)
        circle_dimensions(dictionary)
    elif shape_request == "square":
        dictionary["Shape"].append(shape_request)
        square_dimensions(dictionary)
    elif shape_request == "rectangle":
        dictionary["Shape"].append(shape_request)
        rectangle_dimensions(dictionary)
    elif shape_request == "parallelogram":
        dictionary["Shape"].append(shape_request)
        parallelogram_dimensions(dictionary)
    elif shape_request == "triangle":
        dictionary["Shape"].append(shape_request)
        triangle_dimensions(dictionary)
    elif shape_request == "exit":
        output = pd.DataFrame(dictionary)
        output["Area"].round(2)
        output["Perimeter"].round(2)

        output.to_csv("history.csv")
        exit("Manual program exit")
    else:
        print("Invalid shape")
