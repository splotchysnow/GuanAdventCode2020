# Open the file for the puzzle input and store the data and return the data
def openFile():
    # Maybe for each time headlines == "\n" move it to a different spot to store.
    with open("puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()
    return data


# The rows ranges from 0 to 127
# WORKING PROPERLY!
def seatSearch(word, initialValue, finalPosition, counter=0):
    # There are three different scenario,
    # If the value is happens to be on the first trail, or aka the base case:
    # 2. Find the counter value: and if it matches the length of the word, return the value
    if counter == (len(word) - 1):
        if word[counter] == "F" or word[counter] == "L":
            return initialValue
        elif word[counter] == "B" or word[counter] == "R":
            return finalPosition
        else:
            # print(word[counter])
            return "Do not recognize the object"
    if word[counter] == "F" or word[counter] == "L":
        # 1. Find the middle Number:
        middle = int((1 + (finalPosition - initialValue) / 2))
        middle = middle - 1  # take one down, cuz its f
        middle = middle + initialValue
        counter = counter + 1
        # 5. Recursion                Take out the first letter, counter + 1, initial , mid
        return seatSearch(word, initialValue, middle, counter)
    elif word[counter] == "B" or word[counter] == "R":
        # 1. Find the middle Number:
        middle = int((1 + (finalPosition - initialValue) / 2))
        counter = counter + 1
        middle = middle + initialValue
        return seatSearch(word, middle, finalPosition, counter)
    else:
        return "UNABLE TO UNDERSTAND THE VALUE"


def findBiggestValue(list, position=0, max=0):
    if position == len(list):
        return max
    if list[position] >= max:
        return findBiggestValue(list, position + 1, list[position])
    elif list[position] < max:
        return findBiggestValue(list, position + 1, max)


# ROWS have 0 to 127
# Columns have 0 to 7

def main():
    # Declare data and lines counts. For the parameter.
    data = openFile()
    rowData = []
    columnData = []
    for lines in data:
        if lines[len(lines) - 1] == "\n":

            columnValue = lines[-4:len(lines) - 1]
            rowValue = lines[:-4]

            # #### Debug ####
            # columnSeat = seatSearch(columnValue, 0, 7)
            # rowSeat = seatSearch(rowValue, 0, 127)
            # print("Column Value is", columnSeat)
            # print("Row Value is", rowSeat)
            # print()
            # ### Debug ####

            columnData.append(int(seatSearch(columnValue, 0, 7)))
            rowData.append(int(seatSearch(rowValue, 0, 127)))  # Append the row seat Value into the list
        else:
            columnValue = lines[-3:len(lines)]
            rowValue = lines[:-3]

            # #### Debug ####
            # columnSeat = seatSearch(columnValue, 0, 7)
            # rowSeat = seatSearch(rowValue, 0, 127)
            # print("Column Value is", columnSeat)
            # print("Row Value is", rowSeat)
            # print()
            # ### Debug ####

            columnData.append(int(seatSearch(columnValue, 0, 7)))
            rowData.append(int(seatSearch(rowValue, 0, 127)))  # Append the row seat Value into the list

    # put all the value inside the value data
    counter = 0
    valueData = []

    while True:
        if counter == len(columnData):
            break
        valueData.append((rowData[counter] * 8) + columnData[counter])
        counter += 1

    print(rowData)
    print(columnData)
    print(valueData)
    print(findBiggestValue(valueData))


if __name__ == "__main__":
    main()
