def main():
    with open("Day2/puzzleInput.txt") as f:
        data = f.readlines()
    sentenceCounter = 0 #initalize the counter
    iCounter = 0 #TODO: for debugging Purpose

    #Slicing:
    for i in data:
        #each Line value in data;
        stringEnd = i.find(':') #return position value of the : symbol
        rangeMid = i.find('-') #return the postion value of the - symbol
        rangeBeg = 0 #return the beganning of the sentence;
        rangeEnd = i.find(" ") #find the space

        # print(rangeEnd)
        lowRange = int(i[rangeBeg:rangeMid]) #Got the first value sucessfully
        # print(firstNumber)
        highRange = int(i[rangeMid + 1:rangeEnd]) #Got the second value successfully
        # print(secondNumber)

        #Now I need to get the letter:
        letter = str(i[rangeEnd + 1: stringEnd]) #Success
        #print(letter)

        #Now I need to get the string:
        sentence = str(i[stringEnd + 2: ]) #Success
        # print(sentence)

        letterCounter = 0 # reset the count for the letter valid
        
        iCounter = iCounter + 1 #counting I
        # print(iCounter)

        # if iCounter == 5:
        #     break


        for j in sentence: #loop through each letter
            # print(j) #print each letter in sentence
            if (j == letter): #if the letter == to required letter
                letterCounter += 1 #counter + 1
            
        if ((letterCounter >= lowRange) and (letterCounter <= highRange)): #if the counter is within the range
            sentenceCounter += 1 #sentence Counter + 1
        
        # iCounter += 1
        # if (iCounter == 4): #if I loop through 4 times
        #     break
        

    print(sentenceCounter) # display final result
    






main()