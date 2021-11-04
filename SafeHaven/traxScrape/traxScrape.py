# from trax_login import *
#
#
# def main():
#     trax_login()
#
#
# main()


from user_info import username, password
from datetime import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')

SEARCH_FROM_DATE = driver.find_element_by_css_selector("#searchfromdate")
today = datetime.today()


def trax_login():
    driver.get("https://secure.securitytrax.com/safehaven/login.php?logout=true&ef=L3NhZmVoYXZlbi9jdXN0b21lcnMucGhw")

    driver.find_element_by_id("altxuname").send_keys(username)
    driver.find_element_by_id("altxpass").send_keys(password + Keys.ENTER)

    SEARCH_FROM_DATE.send_keys(today)


def get_year_to_date():
    SEARCH_FROM_DATE.send_keys(today)


trax_login()

