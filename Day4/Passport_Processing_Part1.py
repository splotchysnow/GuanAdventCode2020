import re #getting regular Expression
from Passport import Passport
from typing import List, Sized

#Open the file for the puzzle input and store the data and return the data
def openFile():
    #Maybe for each time readlines == "\n" move it to a different spot to store.
    with open("Day4/puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()
        
    return data


#Count the total amount of people in the passport thing. Probably useless. (Actually its quite useful...)
def listSize(list_):
    return len(list_) #return the size of the list

#Count the amount of empty line inside the puzzle Input to segregate the iformation by people
def emptyLineCount(data):
    count = 0
    arrayCount = []
    for i in data:
        count += 1
        # print(i)
        if i == "\n":
            arrayCount.append(count - 1) #put all the empty line's number in a single list
    arrayCount.append(listSize(data) - 1)
    return arrayCount

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

def infoList(list_, info = "pid"):
    pList = []
    for i in list_:
        pidIIndex = i.find(info)
        temp = i[pidIIndex:] #let a tempreray string = to from pid index to the end of string. find the first space or "\n"
        pidFIndex = temp.find("\n")
        if temp.find(" ") < temp.find("\n"):
            pidFIndex = temp.find(" ")
        pid = temp[4:pidFIndex]
        pList.append(pid)
    return pList



def main():
    data = openFile()
    eLC = emptyLineCount(data)
    personInfoList = cutInfoByPerson(data, eLC) #have the information of each person #TODO: HIS FAULT
    personInfoList = conList(personInfoList) #Store everything into a single 1d Array

    eclList = infoList(personInfoList, "ecl") #store all ecl
    byrList = infoList(personInfoList, "byr") #store all byr
    iyrList = infoList(personInfoList, "iyr") #store all iyr 
    pidList = infoList(personInfoList, "pid") #store all pid
    cidList = infoList(personInfoList, "cid") #store all cid
    hgtList = infoList(personInfoList, "hgt") #store all hgt
    eyrList = infoList(personInfoList, "eyr") #store all eyr
    hclList = infoList(personInfoList, "hcl") #store all hcl
    


    size = listSize(eclList) #get the size of any list for the boundaries of the While Loop
    count = 0 #initalize count to zero

    # firstPerson = Passport(eclList[0], byrList[0], iyrList[0], pidList[0], cidList[0], hgtList[0], eyrList[0], hclList[0])


    #Creating an array of Passports:
    passPortLine = [] #create an empty array of passports   
    while count < size:
        passport = Passport(eclList[count], byrList[count], iyrList[count], pidList[count], cidList[count], hgtList[count], eyrList[count], hclList[count])
        passPortLine.append(passport)
        count = count + 1
    

    print(passPortLine[2].check)

    validCount = 0
    lineCounter = 0 #debug purpose
    invalidList = [] #debug purpose
    for i in passPortLine:
        if i.getCheck() == True: 
            validCount += 1
        if i.getCheck() == False:
            invalidList.append(lineCounter)
        lineCounter += 1 #debugging purpose

    # print(len(invalidList))

    # print(validCount)


    #The answer is between 162 to 290

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

if __name__ == "__main__":
    main()