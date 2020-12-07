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


def treeCount(slopeX, slopeY):
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
               
        #Dubugging Purposes
        # print("Horizontal = ", x , "and Verticle = " , y)
        # print("The Symbole is: ", linesInArray[y][x])
        
        
        # Restrict the X's Boundaries.  If x is about to be > length then restrict it back to 0 # Move x to the right by 3
        if ((x + slopeX) >= (length - 1)):
            remainder = (x + slopeX) - (length - 1)
            x = 0 #reset x back to 0
            x += (remainder)
        else:
            x += slopeX
        


        #move y coordinate
        y += slopeY #move down by 1 line
        
        #exit condition
        if (y >= lineLength):
            break
    return treeCounter


def main():
    answer1 = treeCount(1,1)     # Right 1, down 1.
    answer2 = treeCount(3,1)    # Right 3, down 1. (This is the slope you already checked.)
    answer3 = treeCount(5,1)    # Right 5, down 1.
    answer4 = treeCount(7,1)    # Right 7, down 1.
    answer5 = treeCount(1,2)    # Right 1, down 2.

    print("ANSWER:", answer1 * answer2 * answer3 * answer4 * answer5)


    

if __name__ == "__main__":
    main()