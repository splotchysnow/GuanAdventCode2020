# TO read a file:

with open("Day1/file.txt") as f:
    data = f.readlines()



#Two For Loops to find all value that add up to be 2020;

for i in data:
    for j in data:
        if (i + j == 2020):
            print(i * j)
            break
        else:
            print("I is {i}, J is {j}")