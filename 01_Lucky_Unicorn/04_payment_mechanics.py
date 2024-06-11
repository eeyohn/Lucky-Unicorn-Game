#Lucky Unicorn - payment mechanics

#To do 
#Assume starting amount is $10
#Allow total correctly for a given token
#Adjust total correctly for a given token
#   - if it's a unicorn, add 5
#   - if it's a zebra / horse, subtract 5
#   - if it's a donkey, subtract 1

total = int(input("How much would you like to play with? "))

#Allow manual token input for testing purposes

token = input("Enter a token: ")
#Adjust total correctly for a given token

keep_going = ""
while keep_going == "":

    if token == "unicorn":
        total += 5
        feedback = "Congratulations! You got the lucky unicorn and won $5"

    elif token == "donkey":
        total -= 1
        feedback = "Sorry, You just lost $1"

    else:
        total += 0.5
        feedback = "Congratulations! You won 50c"

    print()
    print(feedback)
    print("You now have {:.2f} to play with".format(total))

    if total < 1:
        print("Sorry, You don't have enough money to continue playing. Game over")
        keep_going = "end"

    else:
        keep_going = input("Press <return> to play again or press any key to quit")

print("Thank you for playing!")