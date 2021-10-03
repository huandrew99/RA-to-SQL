import json

import mysql.connector

from rapt.rapt import Rapt

import sqlite3

def tex_file(filename):
    texFile = open(filename)
    lines = texFile.readlines()
    str = '\t\\textbf{Answer}:\\\\\n'
    res = []
    tempstr = ''
    #print(str)
    i = 0
    for i in range(len(lines)):
        if lines[i] == str:
            i += 1
            while lines[i] != '\t\n':
                tempstr = tempstr + lines[i].strip(' \t$\n') + ';'

                i += 1
            res.append(tempstr)
            tempstr = ''
        #print(lines[i])
    return res


def test():
    return tex_file('test.tex')


def tosql(rastring):
    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)
    f = open('schema.json')
    schema = json.load(f)

    if rastring == ';':
        print('No valid input string')
        return

    return r.to_sql(rastring, schema)


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
    sql_list = produceSqlQuery()
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
    count = 0
    for sql in sql_list:
        count += 1
        print('Question: ')
        tablename = []
        for i, q in enumerate(sql):
            if q.startswith('CREATE'):
                #print(q, "true")
                cursor.execute(q)
                tablename.append(q.split()[3])
                #print(tablename)
                if i == len(sql) - 1:
                    #print(tablename)
                    #print("select * from " + tablename[-1])
                    cursor.execute("select * from " + tablename[-1])
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                    for table in tablename:

                        cursor.execute("drop table " + table)
            else:
                cursor.execute(q)
                result = cursor.fetchall()
                for row in result:
                    print(row)
    cursor.close()

    conn.close()


def driver():
    runsql()


def preprocess(raw):
    i = 0
    j = 0
    result = ""
    firstFind = False
    for j in range(len(raw)):
        if (i < len(raw) and raw[i] == '(' and not firstFind):
            while(raw[i+1] != ')' and i < len(raw)):
                # print("inside")
                i += 1
                # print(raw[i])
                # print(i)
            i += 2
            firstFind = True
        else:
            # print(raw[i])
            if (i < len(raw)):
                result += raw[i]
                i += 1



    return result


def produceSqlQuery():
    rastringlist = test()

    # print(rastringlist[1])
    # print(rastringlist[4])
    sqlstringlist = []
    for rastring in rastringlist:
        try:
            sqlstringlist.append(tosql(rastring))
        except Exception:
            pass

    for sqlstring in (sqlstringlist):
        for i, item in enumerate(sqlstring):
            sqlstring[i] = preprocess(sqlstring[i])

    #for sqlstring in sqlstringlist:
        #print(sqlstring)
    return sqlstringlist


if __name__ == '__main__':

    ins = '\\project_{raptors.name} (raptors \\theta_join_{raptors.happiness = sauropods.happiness} sauropods);'
    stringtest = "Result \\leftarrow \\project_{BranName}(\\s_{State='Indiana' } (LibraryBranch) ); (Result);"

    instring = '\\project_{raptors.name} (raptors \\theta_join_{raptors.happiness = sauropods.happiness} sauropods); \\project_{raptors.name} \\s_{raptors.name="tom"} (raptors);'
    #print(stringtest)
    #print(r.to_sql(stringtest, schema))


    #teststring = preprocess(tosql())

    '''
    
    #test = "WithLoans \\leftarrow \\project_{MembId} (BookLoans);AllMemb \\leftarrow \\project_{MembId} (Member);NoLoans \\leftarrow AllMemb - WithLoans;Result \\leftarrow \\project_{MembName} (NoLoans \\j Member);"
    #print(test)
    print(r.to_sql(test(), schema))
    '''
    #driver()
    #runsql()
    #print(teststring)
    runsqlite()



