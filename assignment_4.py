# assignment 4 divisors
# ask for an input and prints out the numbers it can be 
# devided by

print("Welcome!")
num = int(input("Enter a number: "))

listRange = list(range(1, num+1))

listDivisors = []

# checks for every number in listRange if it can devide with 
# the input number and if so, it pushes them in a new list
for number in listRange:
    if num % number == 0:
        listDivisors.append(number)

print (listDivisors)