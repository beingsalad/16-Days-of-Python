#random is a library which contains many methods like randint(), uniform() etc.
from random import randint #from library import method

my_random = randint(1,50) #random integer
print(my_random) #a random number is thrown at every instance (execution) of the code.

from random import * #importing all methods.
my_random = round(uniform(1,5),1) #random decimals
print(my_random)

my_random = random() #you get a number from 0 to 1 everytime.
print(my_random)

color = ['blue','green','red','yellow']
my_random = choice(color)
print(my_random)

numbers = list(range(5,50,5))
shuffle(numbers) #handy in card names.
print(numbers)

# So well, remember, that shuffle is a method that you can't store in a list.
# It's like all these methods that we've seen that generate an in-place modification on the spot.
# It's actually changing the list.
# So shuffle, we can't use the strings because strings are immutable.

print("\n")
