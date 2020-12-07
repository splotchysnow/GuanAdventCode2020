def openFile():
    with open("Day3/puzzleInput.txt") as f:
        data = f.readlines()
        f.close()
    return data

def storeAsArray(data):
    linesArray = []
    for lines in data:
        linesArray.append(lines)
    return linesArray


#Return the length of a single line in data
def lengthPerLine(data):
    return len(data[0]) # will return the length of the first line in data


def main():

    treeCounter = 0 #Count the amount of trees being hit.

    data = openFile() #I open the file and "data" represent the file.
    
    linesInArray = []
    linesInArray = storeAsArray(data) #store each line in a single array

    length = lengthPerLine(data) #length per each line:
    lineLength = len(linesInArray) 

    # print(length)
    #print(linesInArray)
    #print(lineLength)


    #initiating the coordinate
    x = 0
    y = 0

    while True:
        # print(linesInArray[x][y])

        if (linesInArray[y][x]) == "#":
            treeCounter += 1
            print("Horizontal = ", x + 1 , "and Verticle = " , y + 1)
            print("The Symbole is: ", linesInArray[y][x])   
        
        #Dubugging Purposes
        # print("Horizontal = ", x , "and Verticle = " , y)
        # print("The Symbole is: ", linesInArray[y][x])
        
        
        # Restrict the X's Boundaries.  If x is about to be > length then restrict it back to 0 # Move x to the right by 3
        if ((x + 3) >= (length - 1)):
            remainder = (x + 3) - (length - 1)
            x = 0 #reset x back to 0
            x += (remainder)
        else:
            x += 3
        


        #move y coordinate
        y += 1 #move down by 1 line
        
        #exit condition
        if (y == lineLength):
            break
    print(treeCounter)
    

if __name__ == "__main__":
    main()