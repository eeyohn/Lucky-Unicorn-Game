#Lucky Unicord Decomposition Step 1
#Get initial amount and check that it's valid

#integer checking function
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

keep_going = ""
while keep_going == "":
    how_much = intcheck("How much money do you want to play with? ", 1, 10)
    print("You have chosen to play with ${}".format(how_much))

    keep_going = input("Again? ")