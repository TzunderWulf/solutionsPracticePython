# assignment 7 list comprehensions
# make a new list which contains only the even numbers out of the other list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] # first list with random numbers

b = [x for x in a if x % 2 == 0] # the new list with only the even numbers of list a
print (b)

# or you could immediately print it with 
print([x for x in a if x % 2 == 0])