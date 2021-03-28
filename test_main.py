from unittest import TestCase
from main import getconnection, getnextid, insertrow, process
from mysql.connector import cursor


class Test_getconnection(TestCase):
    def test_getconnection(self):
        conn = getconnection()
        if conn != None:
            self.assertTrue("Got Connection")
        else:
            self.fail()

class Test_getnextid(TestCase):
    def test_getnextid(self):
        next_id = getnextid()
        if next_id > 0:
            self.assertTrue("Got next Id")
        else:
            self.fail()

class Test_insertrow(TestCase):
    def test_insertrow(self):
        conn = getconnection()
        next_id = getnextid(conn)
        insert_string = {"iso_code": "BRA", "continent": "South America", "location": "Brazil", "date": "2020-09-09",
                         "total_cases": "4197889", "new_cases": "35816"}


        insertrow(conn, next_id, insert_string)

        if next_id > 0:
            self.assertTrue("Got next Id")
        else:
            self.fail()

class Test_process(TestCase):
    def test_process(self):
        try:
            process()
        except Exception as e:
            pass


        """
        if next_id > 0:
            self.assertTrue("Got next Id")
        else:
            self.fail()
        
        """