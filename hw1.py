# 1
# startPopulation = 318933342 ##int(input("What is the starting population?"))
def calcUSPopulation(startPopulation):
    seconds_in_year = 31536000
    births_per_year = seconds_in_year // 2
    deaths_per_year = seconds_in_year // 7
    immigrants_per_year = seconds_in_year // 24
    pop_change = births_per_year + immigrants_per_year - deaths_per_year
    new_pop = (startPopulation + pop_change) // 1
    print("The new population is: ")
    return new_pop


# 2
def calcGramsAndKg(gramWeight):
    # Here im floor dividing gram weight to get the number of kilograms in gram.
    X = gramWeight // 1000
    Y = gramWeight % 1000
    print(str(gramWeight) + " is " + str(X) + " kilograms and " + str(Y) + " grams")


calcGramsAndKg(1001)


# 3
# Celsius = (Fahrenheit - 32) * (5/9)
def calcFahrenheit(celsiusTemp):
    farTemp = (celsiusTemp * 9 / 5) + 32
    farTempRounded = str(round(farTemp, 2))
    return farTempRounded


print(calcFahrenheit(20))
