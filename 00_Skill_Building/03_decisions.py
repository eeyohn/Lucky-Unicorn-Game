
keep_going = ""
while keep_going == "":

#Ask user if they like coffee
    like_coffee = input("Do you like coffee?").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print("I like coffee too!")

    elif like_coffee == "no" or like_coffee == "n":
        print("You're missing out!")

    #Print statement if the user inputs an unexpected answer
    else:
        print("I don't understand")

keep_going = input("Press <enter> or any key to quit")
print(keep_going)
          
    

