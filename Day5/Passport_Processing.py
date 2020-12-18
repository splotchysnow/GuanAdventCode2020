# Open the file for the puzzle input and store the data and return the data
def openFile():
    # Maybe for each time headlines == "\n" move it to a different spot to store.
    with open("puzzleInput.txt") as f:
        data = f.readlines()
        # print(data)
        f.close()

    return data


def main():
    # Declare data and lines counts. For the parameter.
    data = openFile()


if __name__ == "__main__":
    main()