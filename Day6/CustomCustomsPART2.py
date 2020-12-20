# Open the file for the puzzle input and store the data and return the data
def openFile():
    # Maybe for each time headlines == "\n" move it to a different spot to store.
    with open("puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()
    return data


def sliceFile():
    with open("puzzleInput.txt") as f:
        names = f.read().split('\n\n')  # anytime the \n show up twice, split it.
    return names


def all_letter_name(data):
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
    return countList


# give back the name for all the repeat values
def nameList(data):
    singleRepeatList = []
    count = 0
    letterList = []
    for line in data:

        if line == "\n":
            singleRepeatList.append(letterList)  # append the count into the count list
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
    singleRepeatList.append(count)  # append the count into the count list
    return singleRepeatList


def find_sum(countList):
    sum_ = 0
    for i in countList:
        sum_ += i
    return sum_


def main():
    responses = sliceFile()
    finalAnswer = []  # Record a list of repeat letters

    for response in responses:
        people = response.split('\n')  # Split each people by new line.
        answer = set(people[0])
        # print("People", people)
        # print("answer", answer)
        # Use &= can generate the intersection of the two sets. <AND Operator>
        counter = 1

        while True:
            if counter == len(people):
                break
            answer &= set(people[counter])  # get the repeated values.
            counter = counter + 1
        finalAnswer.append(len(answer))

    print(finalAnswer)
    print(find_sum(finalAnswer))


if __name__ == "__main__":
    main()

# In this project, I learned how to properly use sets and & operators.
