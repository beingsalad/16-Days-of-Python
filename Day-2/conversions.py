#implicit conversion
num1 = 20
num2 = 10.4

num1 = num1 + num2 #num1 being int is automatically converted into float data type.

print(type(num1))
print(type(num2))

#explicit conversion
num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3) #telling python to change via code.
print(num4)
print(type(num4))

age = input("Tell me your age: ")
print(type(age))

age = int(age)
new_age = 1 + age
print(new_age)

#print("Your new age is going to be "+ new_age) #error
print("Your new age is going to be "+ str(new_age))


