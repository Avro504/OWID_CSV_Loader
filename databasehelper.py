import mysql.connector


def getconnection():
    try:
        conn = mysql.connector.connect(user='dev',
                                       password='Password1',
                                       host='127.0.0.1',
                                       database='Covid-19')
        return conn
    except Exception as e:
        pass


def getnextOWIDid(conn):
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


def insertONSrow(conn, insert_sql):
    cursor = conn.cursor()

    try:
        cursor.execute(insert_sql)
        conn.commit()
        cursor.close()
        pass
    except Exception  as e:
        pass