# assignment 6 string lists
# ask for a string (input of user) and check whether it is a palindrome

word = input("Enter a word: ")
isPalindrome = word[::-1] # turn the word around

if word == isPalindrome:
    print ("Your word is a palindrome (it reads the same for- and backwards)!")
else:
    print("It is not a palindrome.") 