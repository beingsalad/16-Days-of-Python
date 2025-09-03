my_list = ['a', 'b', 'c', 'd']

for letters in my_list:
    print("letter: "+ letters)

for l in my_list:
    print("letter: " + l)

for letter in my_list:
    letter_number = my_list.index(letter) + 1
    print(f"letter {letter_number} : {letter}")

my_list1 = ['Paul', 'John', 'Smith', 'Louis', 'Alexander', 'Laura']
for name in my_list1:
    if name.startswith('L'):
        print(name)
    else:
        print("This name does not begin with 'L'")

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
my_value = 0

for number in numbers:
    my_value = my_value + number

print(my_value) #You defined it outside, but inside the loop, Python keeps reusing and updating that same variable.
#The print(my_value) is outside the loop, so it only prints after the loop finishes (that’s why you see the final total, not the intermediate values).

for number in numbers:
    my_value = my_value + number
    print(my_value) #Now it will print for every iteration and stops when its done.

word = 'python'
for letters in word: #this word variable can be declared in the for loop itself. Check below example.
    print(letters)

for letters in 'python':
    print(letters)

for object in [[1, 2], [3, 4], [5, 6], [7, 8]]: #For each object in this list of lists, it is going to print the object.
    print(object)

for a,b in [[1, 2], [3, 4], [5, 6], [7, 8]]: #it goes to each object and prints a and b (two elements)
    print(a)

dic = {'key1':'a','key2':'b','key3':'c','key4':'d'}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a,b in dic.items():
    print(a,b)

# Exercise 1
students = ["Norville", "Fred", "Velma", "Daphne"]
for i in students:
    print("Hello " + i)

# Exercise 2
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_numbers = 0

for i in list_numbers:
    sum_numbers = sum_numbers + i

print(sum_numbers)

# Exercise 3
# Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:
list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

sum_even = 0
sum_odd = 0

for i in list_numbers:
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i

print(sum_even)
print(sum_odd)

