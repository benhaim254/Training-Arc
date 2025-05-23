import random 

number = random.randint(1,100)


guess = 0
count = 0

while guess != number:
    guess =int(input("Enter Guess: "))
    
    if (guess < number) :
        count+=1
        print ("Guess higher.")
    elif  (guess > number):
        count+=1
        print ("Guess lower.")
    else: 
        count+=1
        print (f"You won. You took only {count} tries to do it.")