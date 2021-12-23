import csv
import smtplib, ssl
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from SafeHaven.AutoMagic.user_info import username, password
import time
import datetime
import os

driver = Chrome()
Chrome(executable_path='/home/avery/.local/bin/chromedriver')

# send_email = "averybou@gmail.com"
# receive_email = ["developeraverybou@gmail.com"]
#
# port = 465  # for SSL
# context = ssl.create_default_context()


def main():

    login_to_quickbase()

    print("Providence Leads:\n")
    download_rep_route("Providence")

    try:
        scrape_csv("Joseph O'Neill 47661")
    except ValueError:
        pass
    try:
        scrape_csv('Ralph Cistoldi 62492')
    except ValueError:
        pass
    try:
        scrape_csv('Ian Sauvageau 39668')
    except ValueError:
        print("ValueError")
        pass
    try:
        scrape_csv('Michael Bottasso 48362')
    except ValueError:
        pass
    try:
        scrape_csv('Edward Hurlburt 49826')
    except ValueError:
        pass
    try:
        scrape_csv('Wilson Delaleu 66073')
    except ValueError:
        pass
    try:
        scrape_csv('Quintin Botelho 64588')
    except ValueError:
        pass
    try:
        scrape_csv('Ian McKinnon 65063')
    except ValueError:
        pass
    try:
        scrape_csv('Avery Bouchard 39819')
    except ValueError:
        pass
    try:
        scrape_csv("Ruben Martins 68653")
    except ValueError:
        pass

    print("Boston Leads:\n")
    download_rep_route("Boston")
    try:
        scrape_csv("Joseph O'Neill 47661")
    except ValueError:
        pass
    try:
        scrape_csv('Ralph Cistoldi 62492')
    except ValueError:
        pass
    try:
        scrape_csv('Ian Sauvageau 39668')
    except ValueError:
        pass
    try:
        scrape_csv('Michael Bottasso 48362')
    except ValueError:
        pass
    try:
        scrape_csv('Edward Hurlburt 49826')
    except ValueError:
        pass
    try:
        scrape_csv('Wilson Delaleu 66073')
    except ValueError:
        pass
    try:
        scrape_csv('Quintin Botelho 64588')
    except ValueError:
        pass
    try:
        scrape_csv('Ian McKinnon 65063')
    except ValueError:
        pass
    try:
        scrape_csv('Avery Bouchard 39819')
    except ValueError:
        pass
    try:
        scrape_csv("Ruben Martins 68653")
    except ValueError:
        pass

    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.ehlo()
    #     server.login(send_email, password)
    #     server.sendmail(send_email, receive_email, message)


def login_to_quickbase():
    driver.get('https://davidyost-7821.quickbase.com/db/main?a=signin')

    username_field = driver.find_element_by_name("loginid")
    password_field = driver.find_element_by_name("password")

    #  input username and password
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.ENTER)


def download_rep_route(office):

    #  navigate to leads page
    driver.get("https://davidyost-7821.quickbase.com/db/bjvssf62r?a=q&qid=214")

    #  Choose office from the dropdown menu
    time.sleep(3)
    drop_down_menu = Select(driver.find_element_by_id("matchTextMC_0"))
    drop_down_menu.select_by_visible_text(office)
    if datetime.date.today().weekday() == 0:
        Select(driver.find_element_by_id("how2_1")).select_by_value("past")
        driver.find_element_by_name("relDateQuant_1").send_keys(Keys.BACKSPACE + "2")

    else:
        drop_down_date_menu = Select(driver.find_element_by_id("how2_1"))
        drop_down_date_menu.select_by_visible_text("yesterday")

    driver.find_element_by_name("display").click()  # click "Display Report" button
    time.sleep(4)
    driver.find_element_by_id("download").click()  # click "Download" button
    time.sleep(2)


# converts the date from today into a string and adds an equation for yesterday's date
def format_date():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    month = str(yesterday).split('-')[1]
    day = str(yesterday).split('-')[2]
    year = str(yesterday).split('-')[0]
    formatted_date = f"{month}-{day}-{year}"

    return formatted_date


def scrape_csv(sales_rep):
    # opens newest file in the Downloads folder
    read_file = get_newest_file()
    read = open(read_file, 'r', encoding='ISO-8859-1')
    csv_read = csv.reader(read)
    # skip the first line of the csv file (header)
    next(csv_read)
    # today = datetime.date.today()
    # dictionary = {}
    nip, nid, gb_appt, nhe_vac, ahs = 0, 0, 0, 0, 0

    # initialize a dictionary for the rep object
    rep = {"Doors Knocked": 0, "Contacts": 0, "Start Time": 0, "End Time": 0, "Sales": 0}

    knock_times = []

    # read through each line of the csv file
    for row in csv_read:
        dictionary = {"Rep": row[1], "Lead Status": row[2], "Visit Time": row[6].split()[1], "Visits": 0, "Contacts": 0,
                      "Start Time": 0, "End Time": 0, "Sales": 0}
        # the following block of code adjusts the visit hour to Eastern Standard Time
        rep_visit_time = dictionary.get("Visit Time").split()[0]
        adj_visit_hour = str(int(rep_visit_time[1]) + 1)
        est_rep_visit_time = str(rep_visit_time[0] + adj_visit_hour + rep_visit_time[2:])

        # check if line contains the rep we are looking for, and if it does...
        if dictionary.get("Rep") == sales_rep:

            # add a knocked door for every line which contains that rep
            rep["Doors Knocked"] += 1

            # gets the first door knocked time and makes that the start time (+1 for EST)
            if rep["Start Time"] == 0:
                rep["Start Time"] = est_rep_visit_time

            # check if lead status insinuates rep spoke to somebody at the door and considers that a contact
            if dictionary.get("Lead Status") == "NID" or dictionary.get("Lead Status") == "NIP" or \
                    dictionary.get("Lead Status") == "GB" or dictionary.get("Lead Status") == "APPT" or \
                    dictionary.get("Lead Status") == "Sold":
                rep["Contacts"] += 1

            # looks for a sold account
            if dictionary.get("Lead Status") == "Sold":
                rep["Sales"] += 1

            # takes the last time with the reps name on it and makes that the end time
            rep["End Time"] = est_rep_visit_time

            if dictionary.get("Lead Status") == "NIP":
                nip += 1
            if dictionary.get("Lead Status") == "NID":
                nid += 1
            if dictionary.get("Lead Status") == "GB" or dictionary.get("Lead Status") == "APPT":
                gb_appt += 1
            if dictionary.get("Lead Status") == "NHE" or dictionary.get("Lead Status") == "VAC":
                nhe_vac += 1
            if dictionary.get("Lead Status") == "AHS":
                ahs += 1

            knock_times.append(dictionary.get("Visit Time"))

            # if dictionary.get("Visit Time") == previous_time or dictionary.get("Visit Time") - previous_time < 1:
            #     print("Less than a minute between doors at " + str(previous_time))

    # prints the rep dictionary to the console as long as there were doors knocked
    if rep["Doors Knocked"] != 0:
        print(sales_rep + ': \nDoors Knocked: ' + str(rep["Doors Knocked"]) + "\nContacts: " +
                              str(rep["Contacts"]) + "\nStart Time: " + str(rep["Start Time"]) + "\nEnd Time: " +
                              str(rep["End Time"]) + "\nSales: " + str(rep["Sales"]) + "\n")
        print(f"NID: {nid}      NIP: {nip}      GB/APPT: {gb_appt}      Empty: {nhe_vac}        Security: {ahs}")
        print("\nKnock Times: ")
        print(*knock_times, sep=", ")
        print("\n\n")


def get_newest_file():
    folder_path = r'/home/avery/Downloads'
    os.chdir(folder_path)
    newest_file = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)[-1]
    return newest_file


main()
# login_to_quickbase()
# download_rep_route("Providence")
# scrape_csv("Joseph O'Neill 47661")
# scrape_csv('Ralph Cistoldi 62492')
# scrape_csv('Ian Sauvageau 39668')
# scrape_csv('Michael Bottasso 48362')
# scrape_csv('Edward Hurlburt 49826')
# scrape_csv('Wilson Delaleu 66073')
# scrape_csv('Quintin Botelho 64588')
# scrape_csv('Ian McKinnon 65063')
# scrape_csv('Avery Bouchard 39819')
# scrape_csv()

driver.close()
