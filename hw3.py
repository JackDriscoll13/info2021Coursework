# HW 3
# 1
def printNumbers(startNum, endNum, stepSize, includeEnd):
    if includeEnd == True:
        for i in range(startNum, endNum + 1, stepSize):
            print(i)
    else:
        for i in range(startNum, endNum, stepSize):
            print(i)


# printNumbers(0,40,5,False)
# 2
def printSomeNumbers(startNum, endNum, divisor):
    # Start with for loop to begin iteration
    for i in range(startNum, endNum + 1):
        if (i % divisor) == 0:
            print("WUBBA LUBBA DUB DUB!")
        else:
            print(i)


# printSomeNumbers(0,20,5)


def printCondimentAd(numAds):
    range1 = (numAds + 1) // 2
    # print(range1)
    count = 0
    for i in range(0, range1):
        print(
            "Ketchup Ad: This red stuff made from tomatoes is better on fries than mayo!"
        )
        count += 1
        # print(count)
        if count != numAds:
            print(
                "Mustard Ad: Golden, spicy, dijon: whichever your flavor, we’ve got the tastes you’ll savor!"
            )
            count += 1
            # print(count)


printCondimentAd(5)

# 4
def zipCodeAd(startZip, endZip):
    for z in range(startZip, endZip + 1):
        if 80300 < z < 80311:
            if (z == 80310) or (z == 80302) or (z == 80309):
                print(
                    "Student Product Ad: Long night studying? Maybe a burrito will ease your pain! Treat yo’ self!"
                )
            else:
                print("Expensive Product Ad: Ur rich buy my shit!")
        else:
            print(
                "Tourist Ad: Come visit Boulder! It’s more beautiful than that place where you live, trust us"
            )


# zipCodeAd(80307,80315)
