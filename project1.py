import random

target = random.randint(1,100)

while True:
    rannum = int(input("Guess the number..."))

    if (rannum == target ):
        print("Success, You have guessed the number!!")    
        break
    elif(rannum > target):
        print("you have guessed a larger number.Guess a smaller number.")
    else:
        print("you have guessed a smaller number.Guess a bigger number.")

        