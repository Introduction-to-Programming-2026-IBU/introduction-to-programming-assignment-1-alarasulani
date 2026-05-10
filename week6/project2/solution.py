# Project 2 — Number Guessing Game
# Author: Irem

import random

# TODO: generate a random secret number between 1 and 10
secret = random.randint(1, 10)

# TODO: set up a guesses counter
guesses = 0

# TODO: get the user's first guess
guess = int(input("Guess a number between 1 and 10: "))

# TODO: while loop — keep asking until the guess is correct
while guess != secret:
    guesses += 1

    if guess < secret:
        guess = int(input("Too low! Try again: "))
    else:
        guess = int(input("Too high! Try again: "))

guesses += 1

# TODO: print the congratulations message with the number of guesses
print(f"Correct! You got it in {guesses} guesses.")
