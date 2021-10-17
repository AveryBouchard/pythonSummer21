from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime
import time
from user_info import username, password
from edit_csv_files import edit_csv_file

driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')

input_file = "./Leads.csv"
output_file = "./Leads_edit.csv"


def login_to_quickbase():
    driver.get('https://davidyost-7821.quickbase.com/db/main?a=signin')

    username_field = driver.find_element_by_name("loginid")
    password_field = driver.find_element_by_name("password")

    #  put these into a separate file for security
    office = "Providence"

    #  input username and password
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.ENTER)

    #  navigate to leads page
    driver.get("https://davidyost-7821.quickbase.com/db/bjvssf6xf?from=myqb")
    leads_link = driver.find_element_by_xpath("/html/body/div[9]/div[12]/ul[1]/li[1]/a")
    leads_link.send_keys(Keys.ENTER)

    #  Choose office from the dropdown menu
    time.sleep(1)
    drop_down_menu = Select(driver.find_element_by_css_selector("#matchTextMC_0"))
    drop_down_menu.select_by_visible_text(office)
    submit_link = driver.find_element_by_id("tableHomePageSearch")
    submit_link.click()

    #  navigate to 2018 Multi Zip
    driver.get("https://davidyost-7821.quickbase.com/db/bjvssf6xv?a=q&qid=906")


def input_zips():
    number_of_reps = int(input("How many lists do you need to make? "))

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

    zip_codes = input("Input zip codes, separated by spaces: ").split()

    return zip_codes


def get_state():
    state = input("What state will they be selling in? (MA or RI) ")

    return state


login_to_quickbase()

input_zips()

edit_csv_file(input_file, output_file, get_state())
