import time
from user_info import username, password
from datetime import datetime, timedelta
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from user_info import SafeHavenEmployee

driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')

month = str(datetime.today()).split('-')[1]
day = str(datetime.today()).split('-')[2]
today = datetime.today().strftime('%m/%d/%Y')
beginning_of_month = datetime.today().replace(day=1)
beginning_of_year = datetime.today().replace(day=1, month=1).strftime('%m/%d/%Y')
last_day_of_last_month = beginning_of_month - timedelta(days=1)
beginning_of_last_month = beginning_of_month - timedelta(days=last_day_of_last_month.day)
beginning_of_month = beginning_of_month.strftime("%m/%d/%Y")
last_day_of_last_month = last_day_of_last_month.strftime('%m/%d/%Y')
beginning_of_last_month = beginning_of_last_month.strftime('%m/%d/%Y')

avery = SafeHavenEmployee("avery",
                          "02901 02903 02905 02907 02909 02910",
                          "Avery Bouchard 39819",
                          f"Avery PVD {month}-{day}",
                          "RI",
                          "39819")
mike = SafeHavenEmployee("mike",
                         "02908 02904 02911 02919 02864 02865",
                         "Michael Bottasso 48362",
                         f"Mike Prov {month}-{day}",
                         "RI",
                         "48362")
ian = SafeHavenEmployee("ian",
                        "02860 02861 02863 02906 02914 02915 02916",
                        "Ian Sauvageau 39668",
                        f"Ian Paw {month}-{day}",
                        "RI",
                        "39668")
quintin = SafeHavenEmployee("quintin",
                            "02740 02744 02745 02746 02743 02719 02738 02739",
                            "Quintin Botelho 64588",
                            f"Q NB {month}-{day}",
                            "MA",
                            "64588")
wilson = SafeHavenEmployee("wilson",
                           "02302 02301",
                           "Wilson Delaleu 66073",
                           f"Wilson Brock {month}-{day}",
                           "MA",
                           "66073")
ian_m = SafeHavenEmployee("ian m",
                          "02720 02721 02723 02724 02725 02726 02791 02790",
                          "Ian McKinnon 65063",
                          f"IanM FR {month}-{day}",
                          "MA",
                          "65063")

providence_team = (avery, mike, ian, quintin, wilson, ian_m)


def trax_login(from_date, to_date="", rep_id=""):
    driver.get("https://secure.securitytrax.com/safehaven/login.php?logout=true&ef=L3NhZmVoYXZlbi9jdXN0b21lcnMucGhw")

    driver.find_element_by_id("altxuname").send_keys(username)
    driver.find_element_by_id("altxpass").send_keys(password + Keys.ENTER)

    search_from_date = driver.find_element_by_name("searchfromdate")
    search_from_date.send_keys(from_date)
    search_to_date = driver.find_element_by_name("searchtodate")
    search_to_date.send_keys(to_date)

    partner_com = driver.find_element_by_id("search_lead_company_id")
    Select(partner_com).select_by_value('8')
    time.sleep(1)
    partner_camp = driver.find_element_by_id("search_lead_company_campaign_id")
    Select(partner_camp).select_by_value("1164")
    sales_rep = driver.find_element_by_id("search_sales_rep_id")
    Select(sales_rep).select_by_value(rep_id)

    driver.find_element_by_name("searchgo").click()


def get_ytd(rep_id=""):
    trax_login(beginning_of_year, rep_id=rep_id)


def get_mtd(rep_id=""):
    trax_login(beginning_of_month, rep_id=rep_id)


def get_last_month(rep_id=""):
    trax_login(beginning_of_last_month, last_day_of_last_month, rep_id)


get_ytd(SafeHavenEmployee.get_rep_id(mike))
