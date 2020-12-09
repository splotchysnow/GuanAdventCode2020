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

def slopeTreeCount( slopeX, slopeY, data):
    treeCounter = 0 #Count the amount of trees being hit.
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
            # print("Horizontal = ", x + 1 , "and Verticle = " , y + 1)
            # print("The Symbole is: ", linesInArray[y][x])   
        
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
    data = openFile() #I open the file and "data" represent the file.
    ans1=slopeTreeCount(1,1,data) # Right 1, down 1.
    ans2=slopeTreeCount(3,1,data) # Right 3, down 1. (This is the slope you already checked.)
    ans3=slopeTreeCount(5,1,data) # Right 5, down 1.
    ans4=slopeTreeCount(7,1,data) # Right 7, down 1.
    ans5=slopeTreeCount(1,2,data) # Right 1, down 2.
    print(ans1*ans2*ans3*ans4*ans5)

  
    
    
    
    

if __name__ == "__main__":
    main()