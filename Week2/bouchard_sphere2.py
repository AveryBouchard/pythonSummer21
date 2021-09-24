"""
Avery Bouchard
9.7.21
Python Programming Sec 061 FA21 AGarside

Sphere Program

Takes in the radius of a sphere and calculates the diameter, circumference, surface area and volume
    of the sphere. Prints all information back out to the terminal.

"""

from math import pi     # import pi from the math module

radius = input("What is the radius of your sphere? ")    # get user input for radius

try:
    radius = float(radius)
    while radius <= 0:
        radius = float(input("Enter a positive number: "))    # if an invalid number is input, asks for another number
except ValueError:
    try:
        radius = float(input("Please try a positive number instead: "))    # gives user another chance to input a number
    except ValueError:
        print("Please restart the program and enter valid inputs.")
        quit()                                                          # quits the program without an error

# formulas based on the radius provided by the user
diameter = round(radius * 2, 2)
circumference = round(diameter * pi, 2)
surfaceArea = round(4 * pi * (radius ** 2), 2)
volume = round(4/3 * pi * (radius ** 3), 2)

# print statements to output to terminal
print("Diameter \t\t :\t", diameter)
print("Circumference \t :\t", circumference)
print("Surface Area \t :\t", surfaceArea)
print("Volume \t\t\t :\t", volume)
