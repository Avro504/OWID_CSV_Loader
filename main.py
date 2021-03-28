import mysql.connector
from insertstring import getinsertstring, getparams


def getconnection():
    try:
        conn = mysql.connector.connect(user='dev',
                                       password='Password1',
                                       host='127.0.0.1',
                                       database='Covid-19')
        return conn
    except Exception as e:
        pass

def getnextid(conn):
    next_id = -1
    try:
        cursor = conn.cursor()
        max_id = cursor.execute("select max(id) from `Covid-19`.OWID_Daily")
        row = cursor.fetchone()
        if row[0] != None:
            next_id = row[0] + 1
        else:
            next_id = 1
    except Exception as e:
        pass

    return next_id

def insertrow(conn, id, valuelist):
    cursor = conn.cursor()
    params = getparams(id, valuelist)
    try:
        insert_string = getinsertstring(valuelist)
        cursor.execute(insert_string, params)
        conn.commit()
        cursor.close()
        pass
    except Exception  as e:
        pass


def process():
    csv_file = open("owid-covid-data.csv", "r")

    conn = getconnection()
    id = getnextid(conn)

    csv_file.readline()     # Headers row
    for line in csv_file:
        line_data = line.strip("\n")
        line_fields = line_data.split(',')
        insertrow(conn, id, line_fields)
        id += 1

    conn.close()
    csv_file.close()




process()