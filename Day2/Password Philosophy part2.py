def main():
    with open("Day2/puzzleInput.txt") as f:
        data = f.readlines()
    sentenceCounter = 0 #initalize the counter
    iCounter = 0 #DEBUG: for debugging Purpose

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


        letterCounter = 0 # reset the count for the letter valid
                
        '''
        OK SO here is the plan: 
            Get J loop through I like last time, everytime J is found. get the position of J and store it in a temperary list
            and then check through that list with the value and see if it matches firstValue and secondValue
            If so GOOD. If not, Invalid
        '''

        # jCounter = 0 #reset counter
        # jList = [] #empty the list
        # for j in i:
        #     if j == letter: #if the J letter matches the letter then get the position
        #         jList.append(jCounter) #Store the position into the list
        #     jCounter += 1 #Counter go up by 1
        
        # #here is where I check if the position excist in the jList:
        # for z in jList:
        #     if (z == firstValue + 1  or z == secondValue +1):
        #         sentenceCounter += 1
        

        #         #DEBUG Can Restrict the amount of looping:        
        # iCounter = iCounter + 1 #counting I
        # # print(iCounter)

        # if iCounter == 5:
        #     break
        #         #DEBUG:
        # print(jList)

        check = False #Reset Check to false
        string1 = i[firstValue] # get the first string position
        string2 = i[secondValue] # get the second string posiiton

        if (string1 == letter): #If else statement for counting
            check = True
        elif (string2 == letter):
            check = True
        else:
            check = False
        
        if check: #if true, count + 1
            sentenceCounter += 1

    print(sentenceCounter)



        






main()