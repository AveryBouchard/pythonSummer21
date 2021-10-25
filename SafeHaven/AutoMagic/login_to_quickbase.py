from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from autoMagic import username, password

driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')


def login_to_quickbase():
    driver.get('https://davidyost-7821.quickbase.com/db/main?a=signin')

    username_field = driver.find_element_by_name("loginid")
    password_field = driver.find_element_by_name("password")

    #  input username and password
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.ENTER)
