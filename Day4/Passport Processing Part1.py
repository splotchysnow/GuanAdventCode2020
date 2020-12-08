def openFile():
    with open("Day4/puzzleInput.txt") as f:
        data = f.readlines()
        f.close()
    return data

#Count the total amount of people in the passport thing. Probably useless.
def countPeople():
    count = 0
    data = openFile()
    for i in data:
        if i == "\n":
            count = count + 1
    return count



def main():
    data = openFile()
    print(data)
    

if __name__ == "__main__":
    main()