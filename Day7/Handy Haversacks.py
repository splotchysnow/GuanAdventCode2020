import re

# Open the file for the puzzle input and store the data and return the data
def openFile():
    # Maybe for each time headlines == "\n" move it to a different spot to store.
    with open("puzzleInput.txt") as f:
        # data = f.read().split()  # split by words
        data = f.read().splitlines() # This makes each line in a single container.
    return data

def bagCollect(data):
    bags = {}

    for line in data:
        color = re.match(r"(.+?) bags contain", line)[1]  # using regular expression.
        bags[color] = re.findall(r"(\d+?) (.+?) bags?", line)
    return bags


data = openFile()
print(bagCollect(data))
