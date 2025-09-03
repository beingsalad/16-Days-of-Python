my_list = ["a","b","c","d","e","f"]
index = 0

for item in my_list:
    print(index, item)
    index += 1 #Not a clear way.

print("\n")
for items in enumerate(my_list):
    print(items)

print("\n")
for index, items in enumerate(range(50,55)):
    print(index,items)

my_list2 = ['a','b','c','d','e','f']
my_tuple = list(enumerate(my_list2))
print(my_tuple)
print(my_tuple[0][1])

# So when you want to access the indexes of an iterable object, consider enumerate as it does in a simple and inexpensive way.

# Exercise 1
# Print sentences like the following on the screen:
# '{name} is found at index {index}'
# Where name must be each of the names in the list below, and the index, must be obtained via enumerate().
list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index, names in enumerate(list_names):
    print(f'{names} is found at index {index}')

# Exercise 2
# Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.
# Call the returned list with the variable name indices_list.
text = "Python"
indices_list = list(enumerate(text))
print(indices_list)

# Exercise 3
# Print to the screen only the indices of those names in the list below, that start with M.
list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
for index,names in enumerate(list_names):
    if names[0] == 'M':
        print(index)