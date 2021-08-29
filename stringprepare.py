import re





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


    print(result)
    return result


def removeExAs(raw):
    sub = "AS"
    res = [i for i in range(len(raw)) if raw.startswith(sub, i)]

    if len(res) > 1:
        res.pop(0)
        print(res)

        changeAmount = 0

        for index in res:
            for i in range(3):
                if len(raw) > index:
                    raw = raw[0: index - changeAmount:] + raw[index - changeAmount + 1::]
            changeAmount += 3

        print(raw)
        return raw
    else:
        return raw


if __name__ == '__main__':
    # string = "CREATE TEMPORARY TABLE librbookcopi(branid, branname, state, bookid, branid, copies) AS SELECT DISTINCT librbran.branid, librbran.branname, librbran.state, bookcopies.bookid, bookcopies.branid, bookcopies.copies FROM AS librbran JOIN  AS bookcopies ON librbran.branid = bookcopies.branid"
    # string = "CREATE TEMPORARY TABLE librbran(branid, branname, state) AS SELECT DISTINCT (this is also need to delete) librarybranch.branid, librarybranch.branname, librarybranch.state FROM librarybranch WHERE state = 'Indiana'"
    # string = "CREATE TEMPORARY TABLE librbookcopi AS SELECT DISTINCT librbran.branid, librbran.branname, librbran.state, bookcopies.bookid, bookcopies.branid, bookcopies.copies FROM  AS librbran JOIN  AS bookcopies ON librbran.branid = bookcopies.branid"
    # stripped = re.sub("[(].*[)]", "", string)
    string = "CREATE TEMPORARY TABLE librbookcopi(branid, branname, state, bookid, branid, copies) AS SELECT DISTINCT librbran.branid, librbran.branname, librbran.state, bookcopies.bookid, bookcopies.branid, bookcopies.copies FROM (SELECT DISTINCT librbran.branid, librbran.branname, librbran.state FROM librbran) AS librbran JOIN (SELECT DISTINCT bookcopies.bookid, bookcopies.branid, bookcopies.copies FROM bookcopies) AS bookcopies ON librbran.branid = bookcopies.branid"
    # print(stripped)
    string = preprocess(string)
    removeExAs(string)

# strlist = ["11", "22", "33"]
# for q in strlist:
#     q = q + "+"
#
# for q in strlist:
#     print(q)