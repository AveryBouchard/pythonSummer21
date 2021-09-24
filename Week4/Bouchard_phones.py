"""
Avery Bouchard
9.7.21
Python Programming Sec 061 FA21 AGarside

phones.py

Program takes user input in the form of a last name or first and last name. It then reads from a file of phone
numbers and determines if the name is in the file. If it is, it returns the name and phone number together
printed to the screen. The program ends when the user doesn't type anything and just presses Enter.
"""

# Get user input for a last name or first and last name
userInput = " "

while userInput != "":          # End program if blank user input
    userInput = input("Enter a last name or first and last name (Just press Enter to quit): ")
    print("\n")

    # Open phones.txt file and read through each line
    file = open("phones.txt", 'r')

    # Assign first name, last name and phone number to split up phones.txt file
    for line in file:
        firstName = line.split()[0].lower()
        lastName = line.split()[1].lower()
        phoneNumber = line.split()[2]

        # Check user input compared to last name OR first and last name
        if userInput.lower() == lastName or userInput.lower() == firstName + " " + lastName:
            # Return phone number for name matching user input
            print(lastName.capitalize() + ", " + firstName.capitalize() + " " + phoneNumber, end="")
            print("\n")
