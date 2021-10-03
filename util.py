import os, random, operator, sys
from collections import Counter

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

def unifyAll(str):
    str = unifytheta(str)

    str = unifyProject(str)
    str = unifyTimes(str)
    str = unifySelect(str)
    str = unifyNaturaljoin(str)
    str = unifyNotEqual(str)
    str = unifyIntersect(str)
    return str

def unifytheta(oldString):
    substring = r"\theta_join_"
    newString = ""
    if substring in oldString:
        newString = oldString.replace(r"\theta_join", "\\theta_join")
        return newString
    else:
        return oldString


def unifyProject(oldString):
    substring = "\pi_"
    newString = ""
    if substring in oldString:
        newString = oldString.replace("\pi_", "\project_")
        return newString
    else:
        return oldString

def unifyTimes(oldString):
    substring = r"\times"
    newString = ""
    if substring in oldString:
        newString = oldString.replace(r"\times", "\j")
        return newString
    else:
        return oldString

def unifySelect(oldString):
    substring = "\sigma"
    newString = ""
    if substring in oldString:
        newString = oldString.replace("\sigma", "\s")
        return newString
    else:
        return oldString

def unifyNaturaljoin(oldString):
    substring = r"\bowtie"
    newString = ""
    if substring in oldString:
        newString = oldString.replace(r"\bowtie", "\\natural_join")
        return newString
    else:
        return oldString

def unifyNotEqual(oldString):
    substring = r"\neq"
    newString = ""
    if substring in oldString:
        newString = oldString.replace(r"\neq", "!=")
        return newString
    else:
        return oldString

def unifyIntersect(oldString):
    substring = "\cap"
    newString = ""
    if substring in oldString:
        newString = oldString.replace("\cap", "\\i")
        return newString
    else:
        return oldString

def containResult(query):
    ContainResult = False
    substring = "result"
    if substring in query:
        ContainResult = True

    return ContainResult