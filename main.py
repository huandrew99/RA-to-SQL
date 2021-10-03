import json

# import mysql.connector

from rapt.rapt import Rapt
from pyparsing import *

import sqlite3

def tex_file(filename):
    texFile = open(filename)
    lines = texFile.readlines()
    # str = '\t\\textbf{Answer}:\\\\\n'
    str = "textbf{Answer}:";
    res = ''


    # i = 0
    # count = 0
    # for i in range(len(lines)):
    #     if lines[i] == str:
    #         i += 1
    #         while lines[i] != '\t\n':
    #             count += 1
    #             res = res + lines[i].strip(' \t$\n') + ';'
    #             i += 1
    # print(count)


    # print("length: ")
    # print(not lines[104])
    # print(len(lines[104]))
    # print("$$" in lines[118])
    # print("$$" in lines[117])
    # print(len(lines[118]))
    # print(not lines[119])
    # print(len(lines[119]))

    i = 0
    count = 0
    for i in range(len(lines)):
        # if lines[i] == str:
        if str in lines[i]:
            # print("is contain true or not: ")
            # print("textbf{Answer}:" in lines[i])
            # print("line number: ")
            # print(i)
            # count += 1
            i += 1
            # while lines[i] != '\t\n':
            while "$" in lines[i]:
                count += 1
                res = res + lines[i].strip(' \t$\n') + ';' + '\n'
                i += 1

    # print("Number of Answer lines: ")
    # print(count)

    return res


def test():
    return tex_file('test2.tex')


def tosql():
    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)
    f = open('schema.json')
    schema = json.load(f)
    strarg = test()
    print(strarg)
    # if strarg == ';':
    #     print('No valid input string')
    #     return
    # # print(strarg + '\n')
    # return r.to_sql(strarg, schema)


# def runsql():
#     sql_list = tosql()
#     print('SQL: Queries')
#     for q in sql_list:
#         print(q)
#     cnx = mysql.connector.connect(user='root', password='root',
#                                   host='localhost',
#                                   database='radb')
#     cursor = cnx.cursor()
#     query = (sql_list[0])
#     cursor.execute(query)
#     result = cursor.fetchall()
#
#     for row in result:
#         print(row)
#     cursor.close()
#     cnx.close()


def runsqlite():
    sql_list = tosql()

    # for q in sql_list:
    #     print(q)
#     print('SQL: Queries')
#
#
#     for q in sql_list:
#         print(q)
#     conn = sqlite3.connect('test.db')
#     cursor = conn.cursor()
#     create_tables = """
# INSERT INTO book VALUES (0, 'Three Bodies', 0);
# INSERT INTO author VALUES (0, 'Cixin Liu');
# INSERT INTO authorbook VALUES (0, 0);
# INSERT INTO publisher VALUES (0, 'Times People', 'Beijing', '11111122');
# INSERT INTO bookcopies VALUES (0, 0, 10000);
# INSERT INTO bookloans VALUES (0, 0, 0, '10/1/2020', '10/1/2021');
# INSERT INTO member VALUES (0, 'Cixin Liu', 'Beijing', '2222211111');
# INSERT INTO librarybranch VALUES (0, 'west lafayette library', 'Indiana');
#     """
#     query = (sql_list[1])
#     cursor.execute(query)
#     result = cursor.fetchall()
#     for row in result:
#         print(row)
#     cursor.close()
#
#     conn.close()


# def driver():
#     runsql()


if __name__ == '__main__':
    #driver()
    runsqlite()



