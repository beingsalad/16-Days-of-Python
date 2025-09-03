#in order to tell python how many times to iterate, we need a list equal to the iterations we need.
# A range is a function that allows you to set a range of numbers without creating a list or even creating a variable.

my_list = [1,2,3,4]
for i in my_list:
    print(i)

print("\n")
for num in range(5):
    print(num)

print("\n")
for num2 in range(20,31,3): #range doesnt take floats in any of its parameters.
    print(num2)

print("\n")
my_list = list(range(1,101)) #101 because we need 100 also.
print(my_list)

print("\n")
# Exercise 1
# Create a list consisting of all the numbers from 2500 to 2585 (inclusive). Store this list in the variable my_list.
my_list = list(range(2500,2586))

# Exercise 2
# Using the range() function, create in a single line of code a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive). Store this list in the variable my_list.
my_list = list(range(3,301,3))

#Exercise 3
# Use the range() function and a loop to add the squares of all the numbers from 1 to 15 (inclusive). Store the result in a variable called sum_squares.
sum_squares = 0

for i in range(1,16):
    sum_squares = sum_squares + i**2
print(sum_squares)