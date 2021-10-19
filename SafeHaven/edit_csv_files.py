import datetime
import csv


def edit_csv_file(read_file, write_file, state="RI"):
    header = ['Last Name','QB Prospect ID','State','First Name','Address','City','Zip','Property Value','Closing Date'
        ,'# 0f Visits','Last Visit','Visit Date','LVS','Appointment Date & TIme','Notes','Notes','Unix Code',
              'Visit Rep','Date Created','Market','Visit - Property Owner 1','Visit - Property Owner 2','Lead Source']

    read = open(read_file, "r")
    write = open(write_file, "w")

    csv_read = csv.reader(read)
    csv_write = csv.writer(write)

    next(csv_read)

    today = datetime.datetime.today()
    two_weeks = datetime.timedelta(days=14)
    one_month = datetime.timedelta(days=30)
    six_months = datetime.timedelta(weeks=48)

    csv_write.writerow(header)

    for row in csv_read:
        if row[10] != 'NHE' or row[10] != 'VAC':
            row[2] = state
            csv_write.writerow(row)

        else:
            split_date = str(row[11].split('-'))
            split_year = split_date[14:18]
            split_month = split_date[2:4]
            split_day = split_date[8:10]

            visit_date = str(split_year + ' ' + split_month + ' ' + split_day)
            visit_date = datetime.datetime.strptime(visit_date, "%Y %m %d")

            empty_date = visit_date + two_weeks
            vacant_date = visit_date + one_month
            off_the_list_date = visit_date + six_months

            if row[10] == "NHE" and today > empty_date or \
                    row[10] == "VAC" and today > vacant_date or \
                    today > off_the_list_date:
                row.clear()

            else:
                csv_write.writerow(row)
