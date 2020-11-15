# assignment 1 character input
# the user puts in their name and age and the program 
# will calculate in which year they will turn 100

print("Welcome!")

# name input
name = input("What is your name? ")

# age input
age = int(input("How old are you? "))

# calculation of what year they will turn 100 in
currentYear = 2020
yearTurnHundred = 2020 + (100 - age)

print(name + " will turn 100 in " + str(yearTurnHundred) + ".")