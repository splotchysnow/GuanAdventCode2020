# TO read a file:

with open("Day1/file.txt") as f:
    data = f.readlines()



#Two For Loops to find all value that add up to be 2020;




# for i in data:
#     for j in data:
#         if (int(i) + int(j) == 2020):
#             print(int(i) * int(j))
#             I = i
#             break
#     if (int(i) == int(I)):
#         break




def main():
    I = -999

    for i in data:
        for j in data:
            for z in data:
                if (int(i) + int(j) + int(z) == 2020):
                    print(int(i) * int(j) * int(z))
                    I = i
                    break
            if (int(i) == int(I)):
                break
        if (int(i) == int(I)):
            break
main()

