# return - It does return a value that we could store in a variable.
def multiply(num1, num2):
    return num1 * num2 #calling this function will return the value of num1 and num2 multiplied to each other.

multiply(5,10) #running this will do nothing, since the function does not have any code that can show something on the screen.
value = multiply(5,200) #Now we can store this value in a variable.
print(value)

def multiply1(num1, num2):
    total = num1 * num2
    return total
total = multiply1(5,10)
print(total)

# Difference between putting print and return inside a custom function:
# print will just show something on the screen and the information dies, once function gets executed.
# return will any type of value, and we can do whatever you want.
def multiply2(num1, num2):
    total2 = num1 * num2
    print(total2)
    return total2
total2 = multiply2(5,10)
print(total2)

#One big problem with function parameters - user might enter different datatype and the function wont get executed.

# Exercise3
# Create a function called reverse_word that takes the characters of a given word as an argument, reverses the order of their characters, and returns them that way and in uppercase.
word = 'Python'
def reverse_word(word):
    return word[::-1].upper()

oh = reverse_word(word)
print(oh)