"""
Avery Bouchard
10.17.21
Python Programming Sec 061 FA21 AGarside

Address Lookup Program

This program imports a list of names, addresses and phone numbers, gets input from the user which they want to loop up,
    takes in a name and returns that person's address or phone number.

"""


#  main function
def main():
    data = add_addresses_to_dict()  # call function to add addresses from file 'address.txt to a dictionary
    information_type = input("Lookup (1) phone numbers or (2) address: ")  # takes input from the user to determine
    # if we will print the address or the phone number

    # starts a while loop to continuously get input from the user
    continue_looping = True
    while continue_looping:
        name_input = input("Enter space-separated first and last name: ").lower()  # user name input
        if name_input == '':  # stops the loop if user doesn't type anything
            continue_looping = False
        if name_input not in data:  # checks whether name is in the dictionary
            print("Name not found, please try again: ")
            continue
        else:
            # if the name is in the dictionary, this for loop will input that key's value to the format and display
            # function
            for name in data:
                if name == name_input:
                    format_and_display_output(data[name], information_type)


'''
Function: add_addresses_to_dict()

Purpose: takes the information from a file (address.txt) and returns it to a dictionary with the first and last name
            of the person as the key, and the rest of the information as the value pair. It also checks to make sure we
            can open the file, and returns an error if not.
            
Parameters: None.

Returns: A full dictionary of key:value pairs. The name is the key, the address and phone number are the value.

'''


def add_addresses_to_dict():
    # attempts to open a file and prints an error code and quits the program if the file does not load
    try:
        addresses = open(r"address.txt", 'r')
    except:
        print("Error code 1")
        quit()

    data = {}  # initialize a blank dictionary

    # loops through each line in the address file to split into name and the rest of the information
    for line in addresses:
        first_and_last_name = line.split(',')[0].lower()  # splits at each comma, takes the 0th index and lowercases it
        address_data = line.split(',')[1:]  # saves the rest of the data as "address_data"
        data[first_and_last_name] = address_data  # saves key value pairs into a dictionary

    return data

'''
Function: format_and_display_output()

Purpose: Once we figure out which key in the dictionary we want to print out, we take the value it is paired with and
            send the information to this function. The function also takes in the type of information the user wants 
            to output and determines whether to print the address or phone number.
            
Parameters: dict_output - this is the value that is associated with the key we have determined we want to return to
                            the user.
            information_type - we ask the user whether they want to lookup the phone number (1) or the address (2) of
                                the person they are looking up.
                                
Returns: None. Outputs formatted information to the console.
'''


def format_and_display_output(dict_output, information_type='1'):
    street, city, state, zip_code, phone_number = dict_output[0], dict_output[1], dict_output[2], dict_output[3], \
                                                  dict_output[4]

    if information_type == '1':
        print("Phone: " + phone_number)

    if information_type == '2':
        print(f"Street:     {street:10}")
        print(f"City:       {city:10}")
        print(f"State:      {state:10}")
        print(f"Zip Code:   {zip_code:10}")


# call the main function to begin the program
main()
