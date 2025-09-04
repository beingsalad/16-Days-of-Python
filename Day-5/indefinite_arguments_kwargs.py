# What is kwargs?
# kwargs stands for “keyword arguments”.
# Just like *args collects extra positional arguments into a tuple,
# **kwargs collects extra keyword arguments into a dictionary.

def a_sum(**kwargs):
    print(type(kwargs))

a_sum(x=3, y=4, z=5)

def a_sum2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

a_sum2(x=3, y=4, z=5)

# What if we want to add up all the values instead of showing up here?
def a_sum3(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        total += value
    return total

print(a_sum3(x=3, y=4, z=5))

#We use **kwargs to pass elements consisting of a key and a value so that they can determine what to do with each of them.
print('\n')

#Merge args and kwargs:
def test(num1, num2, *args, **kwargs):
    # num1 and num2 are normal (positional) parameters.
    print(f"The first number is {num1}")
    print(f"The second number is {num2}")

    # *args collects any extra positional arguments into a tuple
    for arg in args:
        print(f'arg = {arg}')

    # **kwargs collects any keyword arguments into a dictionary
    for key, value in kwargs.items():
        print(f"{key} = {value}")


# A list of extra positional arguments
args = [100, 200, 300, 400]

# A dictionary of keyword arguments
kwargs = {'x': 'one', 'y': 'two', 'z': 'three'}

# Both ways of calling the function:
# Directly providing values
# test(15, 50, 100, 200, 300, 400, x='one', y='two', z='three')

# Or unpacking list/dict into arguments
test(15, 50, *args, **kwargs)


# Exercise1:
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.
def number_attributes(**kwargs):
    count = 0
    for keys, value in kwargs.items():
        count = count + 1
    return count

# Exercise2:
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.
def list_attributes(**kwargs):
    list1 = []
    for key, value in kwargs.items():
        list1.append(value)
    return list1

# Exercise3:
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:
# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...

# #Wrong code:
# def describe_person(*args,**kwargs):
#     for arg in args:
#         for key,value in kwargs.items():
#             return f"Characteristics of {arg}:{key}:{value}" #return inside the first iteration will stop the function immediately after the first arg + first key–value pair. If you want all characteristics, you need to build a result and return after the loops finish.

#Correct one:
def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")
    for key, value in kwargs.items():
            print(f"{key}: {value}")

describe_person(name='A', age=25, height=100)