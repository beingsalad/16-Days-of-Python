minor = min(34,21,48,98,679,31)
major = max(34,21,48,98,679,31)
print(minor)
print(major)

print("\n")
my_list = [58,34,21,98,97]
print(f"The least is {min(my_list)} and the greatest is {max(my_list)}")

print("\n")
names = ['John','Paul','Alicia','Charles']
print(min(names))
print(max(names))

print("\n")
name = 'Charles'
print(min(name))
#Min and Max will look first for the uppercase letters and then the lowercase letters.
name = 'chaRles'
print(min(name))

print('\n')
name = 'John'
print(min(name).lower())

print('\n')
dic ={"Key1":45,"Key2":11}
print(min(dic)) #fetches the minimum key alphabetically.
print(min(dic.values())) #fetches the minimum value.

print("\n")
# Exercise:
# Using max(), min(), and dictionary methods, get the minimum value from the following dictionary:
# dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}
# Store this value in a variable called minimum_age.
# Also, get the name that comes last in alphabetical order, and store it in a variable called last_name.
dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}
minimum_age = min(dictionary_ages.values())
last_name = max(dictionary_ages)
