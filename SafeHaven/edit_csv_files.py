import datetime
import csv

new_state = "MA"
readfile = "./Leads.csv"
writefile = "./Leads_edit.csv"


def edit_csv_file(read_file, write_file, state="RI"):
    read = open(read_file, "r")
    write = open(write_file, "w")

    csv_read = csv.reader(read)
    csv_write = csv.writer(write)
    next(csv_read)

    today = datetime.datetime.today()
    two_weeks_ago = datetime.timedelta(days=14)
    one_month_ago = datetime.timedelta(days=30)
    off_the_list = datetime.timedelta(weeks=48)

    for row in csv_read:
        if row[11] == '':
            row[2] = state
            csv_write.writerow(row)

        else:
            split_date = str(row[11].split('-'))
            split_year = split_date[14:18]
            split_month = split_date[2:4]
            split_day = split_date[8:10]

            visit_date = str(split_year + ' ' + split_month + ' ' + split_day)
            format_date = datetime.datetime.strptime(visit_date, "%Y %m %d")

            empty_date = format_date + two_weeks_ago
            vacant_date = format_date + one_month_ago
            off_the_list_date = format_date + off_the_list

            if row[10] == "NHE" and today > empty_date or \
                    row[10] == "VAC" and today > vacant_date or \
                    today > off_the_list_date:
                row.clear()

            else:
                csv_write.writerow(row)


edit_csv_file(readfile, writefile)

