import random

# This generates a random number and sets randnum to it
randnum = random.randint(1, 20)

# game introduction message
print("Welcome to the guessing game were i'm going to generate a random number between 1-20 and you're going to get "
      "3 tries to try and guess it.")
print("Good Luck! ^_^")

num = 0
count = 1

while count < 4 and num != randnum:
    num = input("Please guess a number between 1-20: ")
    if num == randnum:
        print("You guessed correct. You win!")
    elif num < randnum:
        if count != 3:

