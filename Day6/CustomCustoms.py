# Open the file for the puzzle input and store the data and return the data
def openFile():
    # Maybe for each time headlines == "\n" move it to a different spot to store.
    with open("puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()
    return data


def main():
    data = openFile()
    countList = []
    count = 0
    letterList = []
    for line in data:

        if line == "\n":
            countList.append(count)  # append the count into the count list
            count = 0  # Clear Count
            letterList = []  # Clear the letter list
            # print("Found empty line:")
        else:
            for letter in line:
                if (not (letter in letterList)) and (letter != " ") and (letter != "\n"):
                    # print(letter)
                    count += 1
                    letterList.append(letter)
                else:
                    pass
    countList.append(count)  # append the count into the count list

    sum = 0
    for i in countList:
        sum += i
    print(sum)


if __name__ == "__main__":
    main()
