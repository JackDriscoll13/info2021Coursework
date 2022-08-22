# HomeWork 7
# 1
def writeListToFile(fileName, listOfStuff):
    fileOut = open(fileName, "w")  # opens file for writing
    for stuff in listOfStuff:  # Looks at each item in list
        fileOut.write(stuff + "\n")  # Adds each item to file and then returns new line
    fileOut.close()  # closes file


# 2
import csv


def calculateTestAverage(fileName):
    file = open(fileName, "r")  # opens file for reading
    csvReader = csv.reader(file)  # Opens file in csv reader
    header = next(csvReader)  # skips header
    testCounter = 0  # creating two counters to use in calculation
    scoreCounter = 0
    for line in csvReader:  # looks at each line in csvReader
        testCounter += 1  # adds 1 for each test
        # print(testCounter)
        scoreCounter += int(line[1])  # adds the score of each test
        # print(scoreCounter)
    print(scoreCounter / testCounter)
    file.close()


# 3
def printAssocValue(fileName, searchString):
    file = open(fileName, "r")
    csvReader = csv.reader(file)
    for line in csvReader:
        if line[0] == searchString:
            print(line[1] + "\n")
    file.close()


# 4


def calculateTestScore(fileName, studentName):
    testCounter = 0  # create a counter that counts number of tests for each student
    scoreCounter = 0  # counter that adds test scores for each student
    file = open(fileName, "r")
    csvReader = csv.reader(file)
    header = next(csvReader)  # skips header
    for line in csvReader:  # looks at each line in file
        if line[0] == studentName:  # if student name is first item in line then..
            testCounter += 1  # add one to test scounter
            scoreCounter += int(line[1])  # add score to score counter
    return scoreCounter / testCounter
