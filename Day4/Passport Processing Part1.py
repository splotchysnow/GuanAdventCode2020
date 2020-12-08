import re #getting regular Expression
from typing import List


def openFile():
    #Maybe for each time readlines == "\n" move it to a different spot to store.
    with open("Day4/puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()
        
    return data

#Count the total amount of people in the passport thing. Probably useless.

def listSize(list_):
    return len(list_) #return the size of the list


def emptyLineCount(data):
    count = 0
    arrayCount = []
    for i in data:
        count += 1
        # print(i)
        if i == "\n":
            arrayCount.append(count - 1) #put all the empty line's number in a single list
    return arrayCount

def assignPersonalInfo(list_, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
    for i in list_:
        for j in i: #2nd Dimentions, with all information of passport
            pass

#Display the information in a 2dm array with each person's info in the 2nd dimension
def cutInfoByPerson(data, eLC):
    previous = 0
    list_ = []
    for i in eLC:
        current = i
        list_.append(data[previous:current])
        previous = current
    return list_

#Concavate the 2d array into a 1d array:
def conList(personInfoList):
    list_ = []
    for i in personInfoList:     #concate all the string List into a long giant string
        longString = "" #reset past into an empty string
        for j in i:
            longString += (j + " ") #concavate:
        list_.append(longString)
    return list_


def main():
    data = openFile()
    eLC = emptyLineCount(data)
    personInfoList = cutInfoByPerson(data, eLC) #have the information of each person
    personInfoList = conList(personInfoList) #Store everything into a single 1d Array

    for i in personInfoList:
        print(i.find("pid"))







    








    # print(data)

if __name__ == "__main__":
    main()