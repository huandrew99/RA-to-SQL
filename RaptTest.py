import json
import re

# import mysql.connector

from rapt.rapt import Rapt
from pyparsing import *

import sqlite3


def tex_file(filename):
    texFile = open(filename)
    lines = texFile.readlines()
    str = "textbf{Answer}:";
    res = ''

    i = 0
    count = 0
    for i in range(len(lines)):
        # if lines[i] == str:
        if str in lines[i]:

            i += 1

            while "$" in lines[i]:
                count += 1
                res = res + lines[i].strip(' \t$\n') + ';'
                i += 1

    return res


def test():
    return tex_file('test1.tex')


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


    # print(result)
    return result

def removeExAs(raw):
    sub = "AS"
    res = [i for i in range(len(raw)) if raw.startswith(sub, i)]

    if len(res) > 1:
        res.pop(0)
        # print(res)

        changeAmount = 0

        for index in res:
            for i in range(3):
                if len(raw) > index:
                    raw = raw[0: index - changeAmount:] + raw[index - changeAmount + 1::]
            changeAmount += 3

        # print(raw)
        return raw
    else:
        return raw


def change_to_sql():

    #Q1
    # str = "\project_{BranName}(\s_{State='Indiana' } (LibraryBranch) );"

    #Q2
#     str = """LibrBran \leftarrow \s_{State='Indiana' } (LibraryBranch);
#         LibrBookCopi \leftarrow  LibrBran \\theta_join_{LibrBran.BranId =BookCopies.BranId } BookCopies;
#         LibrBook \leftarrow  LibrBookCopi \\theta_join_{LibrBookCopi.BookId =Book.BookId } Book;
#         Result \leftarrow \project_{Title} (LibrBook);
# """

    #testing
    str = """LibrBran \leftarrow \s_{State='Indiana' } (LibraryBranch);
    LibrBookCopi \leftarrow  LibrBran \\theta_join_{LibrBran.BranId =BookCopies.BranId } BookCopies;
    """

    #Q3
    # str = """
    # WithLoans \leftarrow \project_{MembId} (BookLoans);
    # AllMemb \leftarrow \project_{MembId} (Member);
    # NoLoans \leftarrow AllMemb - WithLoans;
    # Result \leftarrow \project_{MembName} (NoLoans \j Member);"""

    #Q4
    # str = """BAB \leftarrow Book \leftouterjoin_{Book.BookId =AuthorBook.BookId } AuthorBook;
    # BookCop \leftarrow BAB \leftouterjoin_{BAB.BookId =BookCopies.BookId } BookCopies;
    # ABC \leftarrow Author \leftouterjoin_{Author.AuthId =BookCop.AuthId } BookCop;
    # Result \leftarrow \pi_{AuthName, Title, BranId, Copies} (ABC);
    # """

    # #Q5
    # str = """
    # EveryBookWithBranch \leftarrow \pi_{BookId}(BookLoans) \times \pi_{BranId}(LibraryBranch);
    # BookNotEveryBranch \leftarrow \pi_{BookId}(EveryBookWithBranch - \pi_{BookId, BranId}(BookLoans));
    # Result \leftarrow \pi_{BookId}(BookLoans) - BookNotEveryBranch;
    # """

    # #Q6
    # str = """
    # NoCopies \leftarrow \sigma_{Copies=0}(BookCopies);
    # Result \leftarrow \pi_{BookId}(Book) - \pi_{BookId}(BookLoans) - \pi_{BookId}(NoCopies);
    # """

    # #Q7
    # str = """
    # NotBobBooksLoaned \leftarrow \sigma_{AuthName \neq 'Bob'}(Author) \bowtie AuthorBook \bowtie Book \bowtie BookLoans;
    # IllinoisLoaned \leftarrow \sigma_{State='Illinois'}(LibraryBranch) \bowtie NotBobBooksLoaned;
    # IndianaLoaned \leftarrow \sigma_{State='Indiana'}(LibraryBranch) \bowtie NotBobBooksLoaned;
    # BothLoaned \leftarrow IllinoisLoaned \cap IndianaLoaned;
    # Result \leftarrow \pi_{Title}(BothLoaned);
    # """

    strarg = test()


    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)
    f = open('schema.json')
    schema = json.load(f)

    # strarg = strarg.split(";")
    # for str in strarg:
    #     print("Current RA line: ")
    #     print(str)
    #     str = str + ';'
    #     print("Current SQL line: ")
    #     print(r.to_sql(str, schema))

    # print(r.to_sql(str, schema))
    return r.to_sql(str, schema)


if __name__ == '__main__':
    sql_list = change_to_sql()

    print('SQL: Queries')

    for q in sql_list:
        print(q)

    print()
    # conn = sqlite3.connect('test.db')
    # cursor = conn.cursor()
    #
    # # query = (sql_list[1])
    # #
    # # # query = re.sub("[(].*[)]", "", query)
    # # query = preprocess(sql_list[0])
    # # print("This is the new sql")
    # # print(query)
    # #
    # # cursor.execute(query)
    #
    # ContainResult = False
    # substring = "result"
    #
    # for q in sql_list:
    #     if substring in q:
    #         ContainResult = True
    #     query = preprocess(q)
    #     query = removeExAs(query)
    #     print(query)
    #     cursor.execute(query)
    #
    # if ContainResult:
    #     cursor.execute("SELECT * FROM result")
    #
    # if (ContainResult):
    #     print("Contain result")
    # else:
    #     print("not Contain result")
    #
    #
    #
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)
    # cursor.close()
    #
    # conn.close()
