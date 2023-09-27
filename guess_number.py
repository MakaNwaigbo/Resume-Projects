import random

repeat = True 
guessing = True

while repeat:
    rand_num = random.randint(1,10)
    guess_num = int(input(f" I am thinking of a number! Try to guess the number I'm thinking of:"))

    while guessing:
        if guess_num == rand_num:
            again = input("That's it! Would you like to play again? (y/n) ")
            if again == 'no':
                repeat = False
                guessing = False
            elif again == 'yes':
                print("")
                break
        elif guess_num > rand_num:
            guess_num = int(input("Too high! Guess again:"))
        elif guess_num < rand_num:
            guess_num = int(input("Too low! Guess again: "))

print("Thank you for playing!")