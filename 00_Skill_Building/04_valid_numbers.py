#Ask user for a number

valid = False
while not valid:
    error = "Whoops! Please enter an integer"
    try:
        response = int(input("Please enter an integer between 1 and 10: "))
        if 1 <= response <= 10:
            print(response)

        else:
            print(error)
            print()
        valid = True

    except ValueError:
        print(error)
print(response)
