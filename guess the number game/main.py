import art
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
lvl=input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 100)
print("Guess a number between 1 and 100.")

def guess(num):
    if num == number:
        print("You guessed the number!")
    elif num > number:
        print("Too high!")
        print("Guess again")
    else:
        print("Too low!")
        print("Guess again")

if lvl=="easy":
    attempts=11
    while attempts>1:
        print(f"You have {attempts - 1} attempts remaining to guess the number. ")
        guessed = int(input("Your guess: "))
        guess(guessed)
        attempts=attempts-1
        if guessed == number:
            attempts=1
        if attempts==1:
            print("you lost")


elif lvl=="hard":
    attempts=6
    while attempts>1:
        print(f"You have {attempts - 1} attempts remaining to guess the number. ")
        guessed = int(input("Your guess: "))
        guess(guessed)
        attempts = attempts - 1
        if guessed == number:
            attempts = 1
        if attempts==1:
            print("you lost")












