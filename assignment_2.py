# assignment 2 odd or even
# the user puts in a number and divisor and the program checks if
# that is possible

print("Welcome!")

#input number and devisor
inputNum = int(input("Give a number to check: "))
inputDevisor = int(input("Give number to divide by: "))

# checks if the number can be devided by the given devisor
if (inputNum % inputDevisor == 0):
    print (str(inputNum) + " can be devided by " + str(inputDevisor))
else:
    print (str(inputNum) + " can not be devided by " + str(inputDevisor))