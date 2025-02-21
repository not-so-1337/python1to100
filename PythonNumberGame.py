import random

guesscount = 0
num = random.randint(1, 100)
guessed = False
while guessed == False:
    guess = int(input("Guess a number: "))
    guesscount += 1
    if guesscount <= 5:
        if guess == num:
            print("Correct")
            guessed = True
        elif guess != num:
            print("Incorrect")
            if guess > num:
                print("Too high")
            elif guess < num:
                print("Too low")
    elif guesscount >= 5:
        print("You have reached the maximum number of guesses. The correct number was", num)
        guessed = True