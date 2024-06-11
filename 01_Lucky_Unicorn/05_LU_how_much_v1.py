#Lucky Unicorn Fully working program
#SHould work - need to be tested for usability

import random

#Integer checking function below
def intcheck(question, low, high):

    valid = False
    error = "Whoops! Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input("Enter an integer between {} and {}: ".format(low, high)))
            
            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

#main routine

#Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money do you want to play with? ", 1, 10)

keep_going = ""
while keep_going == "":

# tokens list includes 10 items to prevent too many unicorn being chosen
    tokens = ["horse", "horse", "horse",
            "zebra", "zebra", "zebra",
            "donkey", "donkey", "donkey", "unicorn"]

    #Randomly choose a token from the list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    #Adjust total correctly for a given token
    if token == "unicorn":
            balance += 5  # wins $5
            feedback = "Congratulations! You got the lucky unicorn and won $5"

    elif token == "donkey":
            balance -= 1  # doesn't win anything, loses $1
            feedback = "Sorry, You just lost $1"

    else:
            balance += 0.5  # 'wins' 50c, paid $1 so loses 50c
            feedback = "Congratulations! You won 50c"

    print()
    print(feedback)
    print("You now have {:.2f} to play with".format(balance))

    if balance < 1:
            print("Sorry, You don't have enough money to continue playing. Game over")
            keep_going = "end"

    else:
            keep_going = input("Press <return> to play again or press any key to quit")

    print("Thank you for playing!")