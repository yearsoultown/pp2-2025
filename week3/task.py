#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
"""
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

import random

print("Hello, What is your name?")
name = input()
print("Well,", name + ",", "I am thinking of a number between 1 and 20\nTake a guess")

x = random.randint(1, 20)

def guessing(rand, name):
    guess = int(input())
    word = "Take a guess."
    for i in range(1, 21):
        if guess == rand:
            print("Good job,", name + "!", "You guessed my number in", i, "guesses!")
            break
        elif guess < rand:    
            print("Your guess is too low", "\n", word)
            guess = int(input())
        else:
            print("Your guess is too high", "\n", word)
            guess = int(input())

guessing(x, name)