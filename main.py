
from insertstring import getinsertstring, getparams
import ONS_Weeklies
import databasehelper as db


def process():
    csv_file = open("owid-covid-data.csv", "r")

    conn = db.getconnection()
    id = db.getnextOWIDid(conn)

    csv_file.readline()     # Headers row
    for line in csv_file:
        line_data = line.strip("\n")
        line_fields = line_data.split(',')
        params = getparams(id, line_fields)
        insert_string = getinsertstring(line_fields)

        db.insertOWIDrow(conn, id, insert_string, params)
        id += 1

    conn.close()
    csv_file.close()


#process()

ONS_Weeklies.pivot()