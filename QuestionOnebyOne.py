import json
import sqlite3
from util import *

# import mysql.connector

from rapt.rapt import Rapt
from pyparsing import *

import sqlite3

def getallQuestion(numberOfQuestion, filename):
    texFile = open(filename)
    lines = texFile.readlines()
    # str = '\t\\textbf{Answer}:\\\\\n'
    str = "textbf{Answer}:";
    # res = ''
    relations = {}

    i = 0
    count = 0
    for i in range(len(lines)):
        # if lines[i] == str:
        res = ''
        if str in lines[i]:

            i += 1
            count += 1

            while "$" in lines[i]:
                res = res + lines[i].strip(' \t$\n') + ';' + '\n'
                i += 1
            relations[count] = res

    return relations


def raptPrepare():
    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)
    f = open('schema.json')
    schema = json.load(f)
    # return r.to_sql(strarg, schema)
    return r, schema

def getSql(r, schema, strarg):
    return r.to_sql(strarg, schema)

def sqlresult(sql_list):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    ContainResult = False
    substring = "result"

    for q in sql_list:
        if substring in q:
            ContainResult = True
        query = preprocess(q)
        query = removeExAs(query)
        # print("__________________________________")
        # print(query)
        cursor.execute(query)

    if ContainResult:
        cursor.execute("SELECT * FROM result")

    # if (ContainResult):
    #     print("Contain result")
    # else:
    #     print("not Contain result")

    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

def runEachsqlite(numberOfQuestion, latexName):

    # Setup Database


    # Get all relational algebra
    relations = getallQuestion(numberOfQuestion, latexName)
    # print(relations[2]) #store relation for each questions

    # Prepare Rapt
    r, schema = raptPrepare()

    # Define which question skip grading
    skipGrading = [4]

    # iterate all relational algebra
    for i in range(numberOfQuestion):
        if i+1 not in skipGrading:
            print("Question " + str(i+1))
            strarg = relations[i+1]
            strarg = unifyAll(strarg)

            print(strarg)

            sql_list = getSql(r, schema, strarg)


            result = sqlresult(sql_list)
            for row in result:
                print(row)

            print("___________________________________________________________________________")
            print("")


if __name__ == '__main__':
    numberOfQuestion = 7
    latexName = 'test2.tex'
    runEachsqlite(numberOfQuestion, latexName)



