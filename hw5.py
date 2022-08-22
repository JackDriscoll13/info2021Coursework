# Homework 5
# 1
# adds thing to end of list
# uses append command on object of listOfThings
# append adds specific item to end of list
def addAThingToAList(listOfThings, thingToAdd):
    listOfThings.append(thingToAdd)
    print(listOfThings)


# 2


def addToTheFrontOrBack(listOfThings, thingToAdd, addToFront):
    if addToFront == True:
        listOfThings.insert(0, thingToAdd)
    else:
        listOfThings.insert(len(listOfThings), thingToAdd)
    return listOfThings


# 3
# iterates through string, if i == specific letter, counts
def returnLetterCount(aString, letterToFind):
    count = 0  # sets up counter
    for i in aString:
        # looks at each letter
        if letterToFind == i:
            # print(" is the same as "+str(letterToFind))
            count += 1
    return count


# 4
# itereates through list of strings, looks at each string, iterates through each string, looks at letter
# if letter in string is equal to specific letter, adds to count
# prints count
def printLetterCountInList(listOfStrings, letterToFind):
    counter += 0
    for string in listOfStrings:
        # print("string is: "+string)
        for let in string:
            if let == i:
                # print("letter is: "+ str(let))
                counter += 1
    print(counter)
