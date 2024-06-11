#Lucky Unicorn Decomposition Step 3
#Generate a random token

#To Do
#Set up starting amount
#Choose 100 tokens
#   count # of unicorns and multiply by 5
#   count # of horse / zebra and multiply by 0.5
#   count # of donkeys
#   work out total won / lost


import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

uni_count = 0
zebhor_count = 0
donkey_count = 0


for item in range(0, HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        uni_count += 1

    elif chosen == "donkey":
        donkey_count += 1

    else:
        zebhor_count += 1

    print(chosen)

#Money Calculations..

winnings = uni_count * 5 + zebhor_count * 0.5
print("***** Win / Loss Calculations *****")
print("# of Unicorns {}".format(uni_count))
print("# of Zebras / Horses {}".format(zebhor_count))
print("# of Donkeys {}".format(donkey_count))


print()
print("You spent ${}".format(HOW_MUCH))
print("You go home with ${}".format(winnings))