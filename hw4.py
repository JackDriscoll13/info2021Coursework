# Homework 4
# sample list
myList = [
    "phone",
    "wallet",
    "keys",
]
myList.append("tablet")
myList.insert(0, "backpack")
print(myList)
# 1
def printStringItems(listOfStrings):
    for i in listOfStrings:
        print(i)


# printStringItems(["hello", "hi", "two"])
# using index notation:
def printStringItems1(listOfstrings):
    for i in range(0, len(listOfstrings)):
        print(listOfstrings[i])


# printStringItems1(["hello", "hi", "two"])

# 2
def printItemAtIndex(listOfThings, thingIndex):
    thing = listOfThings.pop(thingIndex)
    print(thing)


# printItemAtIndex(myList, 1)


# 3
def printOddOrEven(listOfThings):
    length = len(listOfThings)
    if (length % 2) == 0:
        print("There is an even number of items in the list.")
    else:
        print("There is an odd number of items in the list.")


# 4
def countListCharacters(listOfStrings):
    count = 0
    for i in listOfStrings:
        count += len(i)
    return count


# print(countListCharacters(myList))
