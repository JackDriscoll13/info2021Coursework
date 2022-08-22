# HOMEWORK 8
# 1
def calculateAcceptanceScore(studentData):
    if (
        studentData[-1] == False
    ):  # looks at last item in list which is donor value (true/false)
        standDon = 0
    else:
        standDon = 5
    standSat = (studentData[0] / 160) * (
        0.15
    )  # looks at other important values in list
    standGpa = (studentData[1] * 2) * (0.15)
    standInt = studentData[2] * 0.1
    standCurr = studentData[3] * 0.1
    return round(
        (standDon + standSat + standGpa + standInt + standCurr), 2
    )  # adds important scores togeter, rounds to two dec


# 2
import csv

# create new dictionary for student info
# open and read file
# Look at each line in file (each student)
# get student name  to use as key in dictionary
# get important student scores to pass into calculate func as a list
# pass scores into function as a list
# save the the value of that function in new dictionary w/ student name as key
# close file
# return dictionary for student info
def createAcceptanceDictionary(fileName):
    myDictionary = {}
    myFile = open(fileName, "r")
    csvReader = csv.reader(myFile)  # reads in student data as csv read
    header = next(csvReader)  # skips the first header line
    for line in csvReader:
        studentName = line.pop(
            0
        )  # saves the student name and removes the name from the line
        # for moodle use only:
        if (
            line[8] == "FALSE"
        ):  # I guess we need to do this because passing line[8] as a string or a bool wasnt working
            donval = 0  # sets donval equal to 10 0r 0 based on value of line at index 8
        else:
            donval = 10
        myDictionary[studentName] = calculateAcceptanceScore(
            [float(line[0]), float(line[1]), float(line[2]), float(line[3]), donval]
        )  # updates the dictionary with the sudent name and his acceptance score as a value
    myFile.close()
    return myDictionary


# 3
def calculateAcceptanceScoreSansDonor(studentData):
    donor = studentData.pop(-1)  # pops the donor out of student data
    print(studentData)
    standSat = (studentData[0] / 160) * (0.3)
    standGpa = (studentData[1] * 2) * (0.3)
    standInt = studentData[2] * 0.2
    standCurr = studentData[3] * 0.2
    return round(
        (standSat + standGpa + standInt + standCurr), 2
    )  # same as question 1 except without donor


# 4
def getScores(fileName, studentName):
    donorDictionary = createAcceptanceDictionary(fileName)
    nonDonorDictionary = createAcceptanceDictionarySansDonor(
        fileName
    )  # uses function not in anaconda
    # print(nonDonorDictionary[studentName])
    # print(donorDictionary[studentName])
    rDictionary = {}  # creates dictionary
    rDictionary["Score excluding donor info"] = nonDonorDictionary[studentName]
    rDictionary["Score including donor info"] = donorDictionary[studentName]
    return rDictionary
