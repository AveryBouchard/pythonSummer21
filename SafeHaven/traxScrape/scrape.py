from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import *

driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')

SEARCH_FROM_DATE = driver.find_element_by_id("searchfromdate")
today = datetime.today()


def get_year_to_date():
    SEARCH_FROM_DATE.send_keys(today)
