my_number = 5.8 + 5 #we declare 5.8 as a value to the variable my_number
#my_number = my_number + my_number
print(my_number)

print(type(my_number))


age = input("Tell me your age: ") #Everything the user inputs as a number, is a string. So age will be a string here.
print("Your age is " + age)

print(type(age)) #str data type.

new_age = 1 + int(age) #type conversion.
print(type(new_age)) #int data type.
print("You are going to be " + str(new_age)) #Changing to string again because of string concentation.