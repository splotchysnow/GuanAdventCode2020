def openFile():
    global data
    with open("Day3/puzzleInput.txt") as f:
        data = f.readlines()

def main():
    openFile()

    for i in data: #i represent the each lilne of the data
        for j in i: # for each letter in each line.
            #Should probably declare a counter of some sort.
            count += 1 #counting how much we moved to the right
    






if __name__ == "__main__":
    main()