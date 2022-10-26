import math as m


def circle_dimensions(radius):
    area = m.pi * radius ** 2
    circumference = m.pi * (2 * radius)
    return area, circumference


circle_radius = float(input("What is the radius of circle "))
circle_area, circle_circumference = circle_dimensions(circle_radius)
print("Circle area: {}, circle circumference: {}".format(circle_area, circle_circumference))
