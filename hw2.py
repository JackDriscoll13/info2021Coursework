# HW 2:::
# 1
def calcGramsAndKg(gramWeight):
    if gramWeight < 0:
        print("Invalid number of grams")
    else:
        kilos = gramWeight // 1000
        grams = gramWeight % 1000
        print(
            str(gramWeight)
            + " is "
            + str(kilos)
            + " kilograms and "
            + str(grams)
            + " grams"
        )


# 2
def checkForBiggerNumber(num1, num2):
    if num1 != num2:
        if num1 > num2:
            print("The larger number is " + str(num1))
        else:
            print("The larger number is " + str(num2))
    else:
        print("Numbers are equal!")


# 3
def calcSolarOutput(A, r, H):
    output = A * r * H * 0.75
    # print("Output is " +str(output))
    if output < 8500:
        print(
            "The average annual electricity output for this array is "
            + str(output)
            + " kWh. The array is not sufficient to supply enough electricity to an average home in Colorado."
        )
    else:
        print(
            "The average annual electricity output for this array is "
            + str(output)
            + " kWh. The array is sufficient to supply enough electricity to an average home in Colorado."
        )
