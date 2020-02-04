import random

# This generates a random number and sets randnum to it
randnum = random.randint(1, 20)

# game introduction message
print("Welcome to the guessing game were i'm going to generate a random number between 1-20 and you're going to get "
      "3 tries to try and guess it.")
print("Good Luck! ^_^")

num = 0     # Initializes the num variable variable for the input to 0
count = 1   # Initializes the counter variable for the loop to 1

# This while loop keeps track of the iterations and lets the program know
# what to output and when to escape as well as confirm the number is valid
while count < 4 and num != randnum:
    num = int(input("Please guess a number between 1-20: "))
    if num > 20 or num < 1:
        print("This is not a valid number. Try again")
    else:
        if num == randnum:
            print("You guessed correct. You win!")
        elif num < randnum:
            if count != 3:
                print("Sorry, the number you selected was too low. Try again")
            else:
                print("Sorry, You're out of tries. The correct answer was " + str(randnum) + ". You lose :(")
        else:
            if count != 3:
                print("Sorry, the number you selected was too high. Try again")
            else:
                print("Sorry, You're out of tries. The correct answer was " + str(randnum) + ". You lose :(")

        count += 1  # Increments the counter variable by 1 if its a valid number
