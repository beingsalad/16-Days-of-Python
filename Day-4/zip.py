# What zip basically does is combine two or more lists, interlinking their elements in tuples.
names = ['Hanna', 'Bruce', 'Tony']
ages = [65, 29, 42, 55] #55 wont be zipped.
cities =["New York", "Toronto", "Hamburg"]

combination = zip(names, ages)
print(combination) #result will be <zip object at 0x0000020315951040>.
combination = list(zip(names, ages, cities)) #casting with list to get the output we need.
print(combination)

for name, age, city in combination:
    print(f"{name} is {age} years old, and lives in {city}")

# Exercise1:
# Print to the screen phrases like the following example:
# "The capital of Germany is Berlin"
# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.
capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

combination = list(zip(countries,capitals))

for countries, capitals in combination: # Each tuple like ("Germany", "Berlin") gets unpacked into two variables: countries = "Germany", capitals = "Berlin".
    print(f"The capital of {countries} is {capitals}")

# Exercise2:
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
brands = ["nike","adidas","rebook"]
products = ["nikezoom","superflex","dhonishoes"]

my_zip = zip(brands,products)

# Exercise 3:
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:
# uno / um / one
# dos / dois / two
# tres / três / three
# cuatro / quatro / four
# cinco / cinco / five
spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

numbers = list(zip(spanish, portuguese,english))

print(numbers)

