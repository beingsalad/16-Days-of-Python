print(90/7)
print(round(90/7))

value = round(95.66666666, 3)
print(value)

value2 = round(95.6666666) #It will only be an integer if we round it inside the declaration of the variable.
print(type(value2))

value3 = 95.666666
print(round(value3)) #we are modifying the value outside the round function, so we are just changing the value it will look. Not the value itself.
print(type(value3))
print(value3)

