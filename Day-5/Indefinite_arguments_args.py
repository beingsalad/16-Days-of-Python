# Till now, we were giving definite arguments to python.
# But what if, a function that allows us to add many arguments as we like?
# *args and **kwargs
# Using *args, we can define functions whose number of arguments is variable.
# That is, we can define generic functions that do not accept a certain number of parameters but
# adapt to the number of arguments with which they are called.

# A curious detail is that the use of the args word is actually a convention.
# The code will accept any word you use in its place as long as it starts with a star.
# But it's still a good practice to use ARGs as it helps us understand our code faster.

def a_sum(a,b):
    return a+b

print(a_sum(2,3))
#print(a_sum(2,3, 6 )) #This will throw an error here.

def a_sum2(*args):
    total = 0

    for arg in args:
        total += arg

    return total

print(a_sum2(2,3,4,5,5)) #You can give n number of arguments here.

print("\n")
def a_sum3(*args):
    return sum(args)

print(a_sum3(2,3,4,5,5,1))

#but
print("\n")
def a_sum3(*planes): #args is just a convention. But best practice is using args only.
    return sum(planes)

print(a_sum3(2,3,4,5,5,1,2)) # When you call a_sum3(2,3,4,5,5,1,2), all the values you pass (2, 3, 4, 5, 5, 1, 2) are collected into a tuple called planes.
print("\n")

# So *args doesn’t care whether you pass numbers directly or variables — it only collects the values into a tuple.
# The * in *planes means: “take any extra positional arguments and pack them into a tuple.”

# Exercise1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squares(*args):
    total = 0
    for i in args:           # args is a tuple of all the arguments
        total += i**2        # add square of each number
    return total

print(sum_squares(2,3,4,5,5,1,2))
print("\n")

# Exercise2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0
    for i in args:
        total = total + abs(i)
    return total

print(absolute_sum(2,3,4,5,5,1,2))
print("\n")

# Exercise3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
# The function should return the following message:
# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum_numbers = 0
    for i in args:
        sum_numbers += i
    return f"{name}, the sum of your numbers is {sum_numbers}"

# Summary :
# You can think of *args as a flexible container (a tuple) that collects all the extra values you pass into a function.
# args is the container (tuple) → (10, 20, 30, 40)
# Each item you pass goes inside this container.