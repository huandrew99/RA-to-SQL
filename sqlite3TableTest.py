import json

# import mysql.connector

from rapt.rapt import Rapt
from pyparsing import *

import sqlite3


def createtable():
    str = """CREATE TABLE BOOK
                """

if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # query = "SELECT DISTINCT librarybranch.branid, librarybranch.branname, librarybranch.state FROM librarybranch WHERE state = 'Indiana'"
    query = "CREATE TEMPORARY TABLE librbran AS SELECT DISTINCT librarybranch.branid, librarybranch.branname, librarybranch.state FROM librarybranch WHERE state = 'Indiana'"
    query2 = "CREATE TEMPORARY TABLE librbookcopi AS SELECT DISTINCT librbran.branid, librbran.branname, librbran.state, bookcopies.bookid, bookcopies.branid, bookcopies.copies FROM (SELECT DISTINCT librbran.branid, librbran.branname, librbran.state FROM librbran) AS librbran JOIN (SELECT DISTINCT bookcopies.bookid, bookcopies.branid, bookcopies.copies FROM bookcopies) AS bookcopies ON librbran.branid = bookcopies.branid"

    cursor.execute(query)
    cursor.execute(query2)
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute("SELECT name FROM sqlite_temp_master WHERE type='table';")

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()

    conn.close()
