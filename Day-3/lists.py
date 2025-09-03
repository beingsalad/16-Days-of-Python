my_list = ['a','b','c'] #a list object with 3 elements
another_list = ['hello', 55, 6.1] #contain objects of different data types.
print(type(my_list))

result = len(my_list)
print(result)

#indexing list
result2 = my_list[0:]
print(result2)

#concat list
my_list2 =['d','e','f','g','h']
my_list3 = my_list + my_list2
print(my_list3)

#String manipulation using lists.
my_list3[0] = 'alpha'
print(my_list3)

#Adding something to the original list.
my_list3.append("i")
print(my_list3)

#remove the last element (by default)
my_list3.pop()
print(my_list3)

deleted = my_list3.pop(0)
print(my_list3)
print(deleted)

#sort the list
list1 = ['g','o','b','m','c']
list1.sort() #it reorders the list itself, but its not a method that returns anything.
print(list1)

new_list = list1.sort()
print(new_list) #see, it doesnt return anything here.
print(type(new_list)) #Nonetype indicates that the object has no value.

#So, there are methods that simply do something but do not return information that you can store elsewhere.
list1.sort()
list2 = list1
print(list2)

list1.reverse() #same as sort - Cant store it in any variable.
print(list1)

social_networks = ['YouTube', 'Facebook', 'Twitter', 'Whatsapp']
social_networks.sort() #The function modifies the list in place, without returning a result.



