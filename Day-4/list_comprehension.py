# Dynamic way to build lists.
# Shorter way of writing a for loop that builds a list.

# List comprehension syntax:

# [expression for item in iterable]
#   iterable → something you loop over (like a list, range, etc.)
#   item → internal variable for each element of the iterable
#   expression → what you want to put into the new list



word = 'python'
my_list = []

for letter in word:
    my_list.append(letter)

print(my_list)

#Maybe much simpler?
word = 'python'
my_list = []
my_list = [letter for letter in word] #letter is an internal variable. Could be anything.
# And yes, it looks hard to read, but I think it's very readable because we're here telling Python, that
# I want the variable list to be equal to a composite list.
# Each element is going to be a letter of every letter that's in words.
print(my_list) #one letter for every letter in word.

my_list = [n for n in range(0,21,2)]
print(my_list)

my_list = [n/2 for n in range(0,21,2)]
print(my_list)

#If condition.
my_list = [n for n in range(0,21,2) if n * 2 > 10]
print(my_list)

#If-else condition.
my_list = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(my_list) #the more complex the code, less the readability, more the efficiency.

feet = [10, 20, 30, 40, 50]
meters = [f * 0.3048 for f in feet]
print(meters)

# Exercise1
# Create a square_values list consisting of the numbers in the values list, squared.
values = [1, 2, 3, 4, 5, 6, 9.5]
squared_list = [i **2 for i in values]
print(squared_list)

# Exercise2
# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.
values = [1, 2, 3, 4, 5, 6, 9.5]
even_values = [value for value in values if value % 2 == 0]
print(even_values)

# Exercise3
# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius.
# The conversion between type of units is as follows:
# °C = (°F - 32) * (5/9)
# or expressed in another way:
# (degrees_fahrenheit-32)*(5/9)
temperature_fahrenheit = [32, 212, 275]
degrees_celsius = [(value - 32) * (5/9) for value in temperature_fahrenheit]
print(degrees_celsius)

# List comprehension with if condition:
# [expression for item in iterable if condition]
# "expression" → what you want in the new list
# "for item in iterable" → loop through elements (like a normal for)
# "if condition" → filter (decide which elements to include)

# 👉 Notice: the if comes after the for, because logically it’s applied while looping through each element.

# List comprehension with if..else condition:
# [expression_if_true if condition else expression_if_false for item in iterable]
# Here, if ... else is an expression (decides what value to put in the list).
# The loop runs over every item, but each item might change depending on the condition.
# Nothing is skipped, just transformed.

# Key takeaways:
# If you write if at the end → it’s a filter (include or exclude items).
# If you write if ... else before the for → it’s a choice of value (transform items).


