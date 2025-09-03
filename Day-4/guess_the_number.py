# Number guessing game:
# My solution:
# from random import randint
# name = input("Enter your name: ")
# print(f"Well,{name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")
# secret_number = randint(1,100)
# guess = 0
# while guess < 8 :
#     number = int(input("Enter a number: "))
#     guess +=1
#     if number < 1 or number > 100:
#         print("You have chosen a number that is out of play")
#     elif number > 45:
#         print("The answer is wrong. You have chose a lower number than the secret number.")
#     elif number == 45:
#         print("Congrats! You have guessed the secret number. You took {guess} tries")
#     else:
#         print("Please enter a number between 1 and 100")
#

# Corrected code
# Use clear and separate variable names
secret_number = 45
guess_count = 0

name = input("Enter your name: ")
print(f"Well, {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it.")

while guess_count < 8:
    # Use a different variable for the user's input
    user_guess = int(input("What number do you think it is? "))

    # Increment the counter as soon as a guess is made
    guess_count += 1

    if user_guess < 1 or user_guess > 100:
        print("That number is out of play. Please guess between 1 and 100.")
    elif user_guess > secret_number:
        # Corrected hint
        print("My number is lower.")
    elif user_guess < secret_number:
        # Corrected hint
        print("My number is higher.")
    else:  # This means user_guess == secret_number
        # The count is now correct! And the loop will stop.
        print(f"Congrats, {name}! You have guessed the secret number. You took {guess_count} tries.")
        break  # <-- Important! This stops the game after a win.

# This runs only if the loop finishes without a 'break' (i.e., the user ran out of guesses)
if user_guess != secret_number:
    print(f"Sorry, you've run out of tries. The secret number was {secret_number}.")

print("\n)")

#tutor solution
from random import randint

guess = 0
secret_number = randint(1, 100)
estimation = 0

name = input("Enter your name: ")
print(f"Ok {name}, I have thought of a number between 1 and 100\nYou have 8 guesses to guess")

while guess < 8:
    estimation = int(input("What is the number? "))


    if estimation < secret_number:
        print("My number is higher")
    elif estimation > secret_number:
        print("My number is lower")
    else:
        print(f"Congrats {name}, you have guessed the secret number! You took {guess} tries")
        guess += 1
        break
if estimation != secret_number:
    print(f"Sorry, we have run out of guesses. The secret number was: {secret_number}")