"""
Avery Bouchard
9.7.21
Python Programming Sec 061 FA21 AGarside

Sphere Program

Takes in the radius of a sphere and calculates the diameter, circumference, surface area and volume
    of the sphere. Prints all information back out to the terminal.

"""

import math     # import the math module to get accurate value of pi

pi = math.pi    # save pi from math module as a variable to make it easier to use

radius = 0    # setting radius to zero to enter the while loop

while radius <= 0:
    radius = float(input("What is the radius of your sphere? "))    # get user input for radius

diameter = round(radius * 2, 2)
circumference = round(diameter * pi, 2)
surfaceArea = round(4 * pi * (radius ** 2), 2)
volume = round(4/3 * pi * (radius ** 3), 2)

print("Diameter \t\t :\t", diameter)
print("Circumference \t :\t", circumference)
print("Surface Area \t :\t", surfaceArea)
print("Volume \t\t\t :\t", volume)
