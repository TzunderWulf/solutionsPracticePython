# assignment 8 rock, paper, scissors
# make a two player game of rock, paper, scissors
# ask the players if they wanna continue playing

# welcoming message and explanation
print("Welcome to rock, paper and scissors!\nSetting everything up....")
print("Type 'p' for paper, 'r' for rock and 's' for scissors.\n")
print("Type scores to see the current scores.\nHave fun!\n")

# variables for scores
score_one = 0
score_two = 0

while quit != "N":
    input_one = input("Player one: rock, paper or scissors?\n")
    while input_one != "scores":
        input_two = input("Player two: rock, paper or scissors?\n")
        if (input_one == "r" and input_two == "p" or input_one == "s" and input_two == "r" or input_one == "p" and input_two == "s"):
            print("Player one picked " + input_one + "and player two picked " + input_two)
            print("Player two wins!" + "\n")
        elif (input_one == "r" and input_two == "s" or input_one == "s" and input_two == "p" or input_one == "p" and input_two == "r"):
            print("Player one picked " + input_one + "and player two picked " + input_two)
            print("Player one wins!" + "\n")
        elif (input_one == "r" and input_two == "r" or input_one == "s" and input_two == "s" or input_one == "p" and input_two == "p"):
            print("Player one picked " + input_one + " and player two picked " + input_two)
            print("It's a tie!" + "\n")
        elif (input_two == "scores"):
            print("Player one: " + score_one)
            print("Player two: " + score_two)
            break
        else:
            print("Please type either 'r', 'p' or 's'.")
        
        quit = input("Type 'N' to quit playing or 'Y' to continue.")
        break
    if (input_one == "scores"):
        print("Player one: " + str(score_one))
        print("Player two: " + str(score_two))