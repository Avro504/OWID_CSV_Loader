from datetime import datetime
import databasehelper as db
import insertstring


def read_file():
    csv_file = open("ons.csv", "r")
    global week_number
    global week_ended
    global uk_deaths
    global england_deaths
    global wales_deaths
    global scotland_deaths
    global ni_deaths

    week_number = csv_file.readline().strip("\n").split(",")
    week_ended = csv_file.readline().strip("\n").split(",")
    uk_deaths = csv_file.readline().strip("\n").split(",")
    england_deaths = csv_file.readline().strip("\n").split(",")
    wales_deaths = csv_file.readline().strip("\n").split(",")
    scotland_deaths = csv_file.readline().strip("\n").split(",")
    ni_deaths = csv_file.readline().strip("\n").split(",")

    csv_file.close()

def convertdate(date_string):
    to_date = datetime.strptime(date_string, '%d-%b-%y')
    to_string = to_date.strftime('%Y-%m-%d')
    return to_string

def pivot():
    read_file()
    conn = db.getconnection()
    for i in range(1, len(week_number)):
        insert_sql = insertstring.getONSinsertstring(put the year here, week_number[i], convertdate(week_ended[i]), uk_deaths[i], england_deaths[i], wales_deaths[i], scotland_deaths[i], ni_deaths[i])
        db.insertONSrow(conn, insert_sql)
        pass
