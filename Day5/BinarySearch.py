# This script is mainly for me to remember how to write a  binary search algorithm.

list1 = list(range(1, 100, 2))
# list1 = int(list1)
print(list1)
word = "HELLO WORLD"
print(len(word))
print(word[11])

# lets say I want to search 17
# So yeah, something like this...
def binarySearch(search_list, search_answer, initialValue, finalPosition):
    # There are three different scenario,
    # If the value is happens to be on the first trail, or aka the base case:

    # Set the position some how.
    position = int(1 + (finalPosition - initialValue) / 2)

    if search_list[position] == search_answer:
        print("Position of the list is:", position)
        return position

    elif search_answer > search_list[position]:
        # If the Search answer is larger than what we have at the current position
        # Recursion
        return binarySearch(search_list, search_answer, position, finalPosition)

    elif search_answer < search_list[position]:
        return binarySearch(search_list, search_answer, initialValue, position)

    else:
        # There is no element in the array.
        return -1


binarySearch(list1, 17, 0, len(list1))
binarySearch(list1, 29, 0, len(list1))

print(list1[14])