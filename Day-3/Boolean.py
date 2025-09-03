var1 = True #declare the variable explicitly.
var2 = False
print(type(var1))
print(var1)

number = 5 > 2 + 3 #implicit.
print(number)
print(type(number))
print("---")
number = 5 >=  2 + 3
print(number)
print(type(number))
print("---")
number = 5 !=  2 + 3
print(number)
print(type(number))
print("---")
number = bool(5 > 6)
print(number)
print(type(number))
print("---")
list = [1,2,3,4]
control = 5 not in list
print(control)
print(type(control))