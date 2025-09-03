# You work in a company where salespeople receive 13% commissions on their total sales, and your boss wants you to help the salespeople calculate their commissions by creating a program that asks them their name and how much they've sold this month.
# Your program will answer them with a sentence that includes their name and the amount of commissions they are entitled to.

# Guidelines:
# This program should start by asking the user for things.
# So you're going to need to use input to receive user input, and you should use variables to store that input.

# Remember that user inputs are stored as strings, so you should convert one of those inputs to float to be able to do operations on it.
# And what operation do you need to do? Well, calculate 13% of the number that the user has entered.
# That is, multiply the number by 13, then divide by 100.

# It would be good to print the result on the screen, so make sure this information has no more than two decimals.
# So it is going to be easy to read and then organize all that in a string that you would format.

name = input("Please, tell me your name: ")
sales = int(input("Please, input your total month sales: "))
commission = round(sales * 0.13, 2)

print(f"Hello {name}, your commission this month are ${commission}")

