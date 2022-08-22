# HomeWork 6
# 1
def printNumLinesInFile(fileName):
    filehand = open(str(filename), "r")
    fileCont = filehand.read()
    filehand.close()
    listoflines = fineCont.splitlines()
    print(len(listoflines))


# 2
def printNumWordsInFile(fileName):
    myFile = open(str(fileName), "r")
    Fcontents = myFile.read()
    myFile.close
    wordList = Fcontents.split()
    print(len(wordList))


# 3
def processTweetFile(fileName):
    # Open the file for reading
    myFile = open(str(fileName), "r")
    # Get the file contents in a string
    fContents = myFile.read()
    # close the file
    myFile.close
    # count the number of times "#" appears in file string
    num = fContents.count("#")
    # print the number
    print(num)


# 4
def processFiles(listOfFileNames):
    wordCounter = 0
    for fileName in listOfFileNames:
        fileHand = open(str(fileName), "r")
        fileContents = fileHand.read()
        fileHand.close()
    print(wordCounter)
