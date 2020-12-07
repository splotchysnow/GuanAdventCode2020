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
    count = 0 # Count for the current postion in x

    data = openFile() #I open the file and "data" represent the file.
    
    linesInArray = []
    linesInArray = storeAsArray(data) #store each line in a single array

    length = lengthPerLine(data) #length per each line:
    lineLength = len(linesInArray) 

    #print(linesInArray)



    print(lineLength)
    #slope -> Right 3 and down 1;

    x = 0
    y = 0

    while True:
        print(linesInArray[x][y])
        x += 3
        y += 1
        if (y == lineLength):
            break

    

if __name__ == "__main__":
    main()