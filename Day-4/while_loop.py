#They repeat while a condition is met.
coins = 5

while coins > 0:
    print(f" I have {coins} coins") #If we leave in this step, the loop will never end since value of the variable is not changing.
    coins -= 1  # coins = coins - 1 #So, we do this.
else:
    print("I have no money anymore")

print('\n')
answer = "yes"
while answer == "yes":
    answer = input("Do you want to continue? (yes/no) ")
else:
    print("Thank you")

#Keywords - pass, break and continue.
#PASS - do nothing. Its just a placeholder

# answer = ("y")
#
# while answer == "y":
#     pass #If i dont write pass here, it will give me an error, since there's no action to be performed.
#
#
# print("Hello")

#BREAK - Interrupting the current iteration of the loop we are in and go straight out of the loop
name = input("Your name")

for letter in name:
    if letter == 'e':
        break
    print(letter)

#Continue - Interrupts the current iteration but does not interrupt the loop itself.
for letter in name:
    if letter == 'e':
        continue #when e comes, it skips and goes back to the beginning of the code and continues with the next iteration.
    print(letter)


# Exercise 1
number = 10
while number >= 0:
    print(number)
    number = number - 1

# Exercise 2
number = 50

while number >= 0 :
    if number % 5 == 0:
        print(number)
    else:
        pass
    number -= 1 # number = number - 1

# Exercise 3
list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for i in list_numbers:
    if i >= 0:
        print(i)
    else:
        break
