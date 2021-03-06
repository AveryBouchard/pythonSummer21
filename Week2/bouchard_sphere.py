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

while True:
    try:
        radius = float(radius)
        while radius <= 0:
            radius = float(input("Please enter a positive number: "))   # if an invalid number is input, asks for another number
        break
    except ValueError:
        pass

    print("Input is not a number, try again.")

# formulas based on the radius provided by the user
diameter = round(radius * 2, 2)
circumference = round(diameter * pi, 2)
surfaceArea = round(4 * pi * (radius ** 2), 2)
volume = round(4/3 * pi * (radius ** 3), 2)

# print statements to output to terminal
print(f"Diameter \t\t :\t", diameter)
print("Circumference \t :\t", circumference)
print("Surface Area \t :\t", surfaceArea)
print("Volume \t\t\t :\t", volume)
