from selenium.webdriver import Chrome
driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')


def input_zips():
    number_of_reps = int(input("How many reps will you input zips for? "))

    text_field_number, reps = 0, 0

    #  gives the option to input zip codes for multiple reps
    while reps < number_of_reps:

        zip_code_input = get_zips()

        #  loops through all input zip codes
        for zip_code in zip_code_input:

            #  adds the number of the text field to the end of the element name
            zip_input_field = driver.find_element_by_name("matchText_" + str(text_field_number))

            zip_input_field.send_keys(zip_code)

            #  increment the text field number to go down to the next field
            text_field_number += 1

        reps += 1

        display_report_button = driver.find_element_by_id("saveButton")

        display_report_button.send_keys(Keys.ENTER)

        time.sleep(1)

        download_button = driver.find_element_by_id("download")

        download_button.send_keys(Keys.ENTER)  # download the CSV file

        time.sleep(1)

        driver.back()  # go back to multi zip page

        text_field_number = 0

        time.sleep(1)

        driver.find_element_by_name("matchText_0").clear()


def get_zips():

    zip_codes = list(input("Input zip codes, separated by spaces: ").split())

    return zip_codes