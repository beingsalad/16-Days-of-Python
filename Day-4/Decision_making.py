if 10 > 9: #if executes the print statement within, only if the condition is True.
    print('It is correct')
if True:
    print('It is correct')

x = True
if x:
    print('It is correct')

if 5 == 2: #It won't even execute, since condition here is false.
    print('It is correct')
else: #This will execute now.
    print("It is incorrect")

pet = "Dog"
if pet == "cat":
    print("You have a cat")
elif pet == "dog":
    print("You have a dog")
elif pet == 'rabbit':
    print("You have a rabbit")
else:
    print("I dont know what animal you have")

age = 16
school_grade = 9

if age < 18:
    print("You are a minor")
    if school_grade >=7:
        print("Passed")
    else:
        print("Failed")
else:
    print("You are an adult")

#Exercise1:
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

#Exercise2:
age = 16
has_license = False

if age >= 18:
    print("You can drive")
elif age < 18:
    print("You can't drive yet. You must be 18 years old and have a license")
else:
    print("You can't drive. You need to have a license")

#Exercise3:
speak_french = True
knows_python = False

if (speak_french == True) and (knows_python == True):
    print("You meet the requirements to apply")
elif (speak_french == False) and (knows_python == True):
    print("To apply, you need to speak French")
elif (speak_french == True) and (knows_python == False):
    print("To apply, you need to know how to program in Python")
else:
    print("To apply, you need to know how to program in Python and speak French")