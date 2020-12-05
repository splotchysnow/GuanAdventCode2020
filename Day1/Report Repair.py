# TO read a file:

with open("Day1/file.txt") as f:
    data = f.readlines()



#Two For Loops to find all value that add up to be 2020;


I = -999

for i in data:
    for j in data:
        if (int(i) + int(j) == 2020):
            print(int(i) * int(j))
            I = i
            break
    if (int(i) == int(I)):
        break

