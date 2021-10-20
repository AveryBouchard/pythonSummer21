from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def get_zips():

    zip_codes = list(input("Input zip codes, separated by spaces: ").split())

    print(zip_codes)

    return zip_codes


zips = get_zips()


driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')


def login_to_quickbase():

    driver.get('https://davidyost-7821.quickbase.com/db/main?a=signin')

    username_field = driver.find_element_by_name("loginid")
    password_field = driver.find_element_by_name("password")

    #  put these into a separate file for security
    username = "ABouchard@mysafehaven.com"
    password = "Duarte1986!"
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


def input_zips(zip_code_input):

    text_field_number = 0

    for zip_code in zip_code_input:

        zip_input_field = driver.find_element_by_name("matchText_" + str(text_field_number))

        zip_input_field.send_keys(zip_code)

        text_field_number += 1

    display_report_button = driver.find_element_by_id("saveButton")

    display_report_button.send_keys(Keys.ENTER)

    time.sleep(1)

    download_button = driver.find_element_by_id("download")

    download_button.send_keys(Keys.ENTER)


login_to_quickbase()

input_zips(zips)




