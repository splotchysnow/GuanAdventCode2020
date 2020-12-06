def main():
    with open("Day2/puzzleInput.txt") as f:
        data = f.readlines()
    sentenceCounter = 0 #initalize the counter
    # iCounter = 0 #DEBUG: for debugging Purpose

    #Slicing:
    for i in data:
        #each Line value in data;
        stringEnd = i.find(':') #return position value of the : symbol
        rangeMid = i.find('-') #return the postion value of the - symbol
        rangeBeg = 0 #return the beganning of the sentence;
        rangeEnd = i.find(" ") #find the space

        # print(rangeEnd)
        firstValue = int(i[rangeBeg:rangeMid]) #Got the first value sucessfully
        # print(firstNumber)
        secondValue = int(i[rangeMid + 1:rangeEnd]) #Got the second value successfully
        # print(secondNumber)

        #Now I need to get the letter:
        letter = str(i[rangeEnd + 1: stringEnd]) #Success
        #print(letter)

        #Now I need to get the string:
        sentence = str(i[stringEnd + 2: ]) #Success
        # print(sentence)


        check = False #Reset Check to false
        string1 = sentence[firstValue - 1] # get the first string position
        string2 = sentence[secondValue - 1] # get the second string posiiton

        # print(string1)
        # print(string2)
        # print(letter)

        if (string1 == letter and string2 == letter): #If else statement for counting
            check = False
        elif (string2 == letter or string1 == letter):
            check = True
        else:
            check = False
        if check: #if true, count + 1
            sentenceCounter += 1

    print(sentenceCounter)

main()