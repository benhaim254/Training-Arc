import random 

min = 1
max = 6

roll = input(("Want to roll the dice? "))

while roll == "yes" or roll == "y":
    print ("Rolling the dice.....")
    print ("The values are ....")
    print (random.randint (min,max))
    print (random.randint (min,max))
    
    roll = input(("Roll again? "))
else:
    print("Thanks for coming by. See you again later.")
