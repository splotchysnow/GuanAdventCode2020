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


def main():
    data = sliceFile()



if __name__ == "__main__":
    main()

# In this project, I learned how to properly use sets and & operators.
