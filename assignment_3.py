# assignment 3 list less than 10
# first challenge: print the elements that are less than 5 in listNumbers

listNumbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in listNumbers:
    if (x <= 5):
        print (x)

# second challenge: print the element that are less than an input 
# given in listNumbers

print ("Welcome!")
num = input("Give a number: ")

for x in listNumbers:
    if (x <= int(num)):
        print (x)

# third challende: write the code in one line (not done yet)
