# import re  # getting regular Expression
from Passport import Passport


# from typing import List, Sized


# Open the file for the puzzle input and store the data and return the data
def openFile():
    # Maybe for each time headlines == "\n" move it to a different spot to store.
    with open("puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()

    return data


# Count the total amount of people in the passport thing. Probably useless. (Actually its quite useful...)
def listSize(list_):
    return len(list_)  # return the size of the list


# Count the amount of empty line inside the puzzle Input to segregate the information by people
def emptyLineCount(data):
    count = 0
    arrayCount = []
    for i in data:
        count += 1
        # print(i)
        if i == "\n":
            arrayCount.append(count - 1)  # put all the empty line's number in a single list
    arrayCount.append(listSize(data) - 1)
    return arrayCount


# Display the information in a 2dm array with each person's info in the 2nd dimension
def cutInfoByPerson(data, elc):
    previous = 0
    list_ = []
    for i in elc:
        current = i
        list_.append(data[previous:current])
        previous = current
    return list_


# Concave the 2d array into a 1d array:
def conList(person_info_list):
    list_ = []
    for i in person_info_list:  # concat all the string List into a long giant string
        longString = ""  # reset past into an empty string
        for j in i:
            longString += (j + " ")  # concave:
        list_.append(longString)
    return list_


def infoList(list_, info="pid"):
    pList = []
    for i in list_:
        pidIIndex = i.find(info)
        temp = i[
               pidIIndex:]  # let a temporary string = to from pid index to the end of string. find the first space
        # or "\n"
        pidFIndex = temp.find("\n")
        if temp.find(" ") < temp.find("\n"):
            pidFIndex = temp.find(" ")
        pid = temp[4:pidFIndex]
        pList.append(pid)
    return pList


def main():
    # Declare data and lines counts. For the parameter.
    data = openFile()
    eLC = emptyLineCount(data)
    personInfoList = cutInfoByPerson(data, eLC)  # have the information of each person
    personInfoList = conList(personInfoList)  # Store everything into a single 1d Array

    # Lists
    eclList = infoList(personInfoList, "ecl")  # store all ecl
    byrList = infoList(personInfoList, "byr")  # store all byr
    iyrList = infoList(personInfoList, "iyr")  # store all iyr
    pidList = infoList(personInfoList, "pid")  # store all pid
    cidList = infoList(personInfoList, "cid")  # store all cid
    hgtList = infoList(personInfoList, "hgt")  # store all hgt
    eyrList = infoList(personInfoList, "eyr")  # store all eyr
    hclList = infoList(personInfoList, "hcl")  # store all hcl

    # Finding Size and Counting!
    size = listSize(eclList)  # get the size of any list for the boundaries of the While Loop
    count = 0  # initialize count to zero
    # firstPerson = Passport(eclList[0], byrList[0], iyrList[0], pidList[0], cidList[0], hgtList[0], eyrList[0],
    # hclList[0]) Creating an array of Passports:
    passPortLine = []  # create an empty array of passports
    while count < size:
        passport = Passport(eclList[count], byrList[count], iyrList[count], pidList[count], cidList[count],
                            hgtList[count], eyrList[count], hclList[count])
        passPortLine.append(passport)
        count = count + 1
    validCount = 0
    lineCounter = 0  # debug purpose
    invalidList = []  # debug purpose
    for i in passPortLine:
        if i.checkInvalidPassport():
            validCount += 1
        if not i.checkInvalidPassport():
            invalidList.append(lineCounter)
        lineCounter += 1  # debugging purpose

    for i in passPortLine:
        print(i.hclChecker())
    # The Result!
    print("The Count is:", validCount)


def debug():
    # print(passPortLine[2].check)
    # print(passPortLine[0].)
    # print(len(invalidList))
    # print(passPortLine[0].existenceChecker())
    # #print(passPortLine[0].checkInvalidPassport())
    # print(passPortLine[0].byrChecker())
    # print(passPortLine[0].cidChecker())
    # print(passPortLine[0].eclChecker()) #return none
    # print(passPortLine[0].eyrChecker())
    # print(passPortLine[0].hclChecker())
    # print(passPortLine[0].hgtChecker()) #return None
    # print(passPortLine[0].iyrChecker())
    # print(passPortLine[0].pidChecker()) #return None

    # The answer is between 162 to 290

    # #debug
    # print(eLC)
    # print(personInfoList)
    # print(eclList[-1])
    # print(byrList[-1])
    # print(iyrList[0])
    # print(pidList[0])
    # print(cidList[0])
    # print(hgtList[0])
    # print(eyrList[0])
    # print(hclList[0])
    # print(data)

    # These use to test the independent tests.
    # print(passPortLine[0].hgtChecker())
    # print(passPortLine[0].getHgt())

    pass


if __name__ == "__main__":
    main()
