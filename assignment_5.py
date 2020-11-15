# assignment 5 lists overlap
# takes list numbers and makes a new list (evenNumbers) with
# only the even elements out of list numbers

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [x for x in a if x % 2 == 0]
print (b)

# or you could immediately print it with
print([x for x in a if x % 2 == 0])