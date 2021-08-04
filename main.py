import json

import mysql.connector

from rapt.rapt import Rapt

import sqlite3

def tex_file(filename):
    texFile = open(filename)
    lines = texFile.readlines()
    str = '\t\\textbf{Answer}:\\\\\n'
    res = ''
    print(str)
    i = 0
    for i in range(len(lines)):
        if lines[i] == str:
            i += 1
            while lines[i] != '\t\n':
                res = res + lines[i].strip(' \t$\n') + ';'

                i += 1
        #print(line)
    return res


def test():
    return tex_file('test.tex')


def tosql():
    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)
    f = open('schema.json')
    schema = json.load(f)
    strarg = test()
    if strarg == ';':
        print('No valid input string')
        return
    print(strarg + '\n')
    return r.to_sql(strarg, schema)


def runsql():
    sql_list = tosql()
    print('SQL: Queries')
    for q in sql_list:
        print(q)
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='radb')
    cursor = cnx.cursor()
    query = (sql_list[0])
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    cnx.close()


def runsqlite():
    sql_list = tosql()
    print('SQL: Queries')
    for q in sql_list:
        print(q)
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    create_tables = """
INSERT INTO book VALUES (0, 'Three Bodies', 0);
INSERT INTO author VALUES (0, 'Cixin Liu');
INSERT INTO authorbook VALUES (0, 0);
INSERT INTO publisher VALUES (0, 'Times People', 'Beijing', '11111122');
INSERT INTO bookcopies VALUES (0, 0, 10000);
INSERT INTO bookloans VALUES (0, 0, 0, '10/1/2020', '10/1/2021');
INSERT INTO member VALUES (0, 'Cixin Liu', 'Beijing', '2222211111');
INSERT INTO librarybranch VALUES (0, 'west lafayette library', 'Indiana');
    """
    query = (sql_list[1])
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()

    conn.close()


def driver():
    runsql()


if __name__ == '__main__':

    ins = '\\project_{raptors.name} (raptors \\theta_join_{raptors.happiness = sauropods.happiness} sauropods);'
    stringtest = "Result \\leftarrow \\project_{BranName}(\\s_{State='Indiana' } (LibraryBranch) ); (Result);"

    instring = '\\project_{raptors.name} (raptors \\theta_join_{raptors.happiness = sauropods.happiness} sauropods); \\project_{raptors.name} \\s_{raptors.name="tom"} (raptors);'
    #print(stringtest)
    #print(r.to_sql(stringtest, schema))



    '''
    #print(test())
    #test = "WithLoans \\leftarrow \\project_{MembId} (BookLoans);AllMemb \\leftarrow \\project_{MembId} (Member);NoLoans \\leftarrow AllMemb - WithLoans;Result \\leftarrow \\project_{MembName} (NoLoans \\j Member);"
    #print(test)
    #print(r.to_sql(test, schema))
    '''
    #driver()
    runsqlite()



