my_dictionary = {'c1':'value1', 'c2':'value1'} #keys have to be unique but values dont have to.
print(type(my_dictionary))
print(my_dictionary)

result1 = my_dictionary['c1'] #invoking the key 'c1'
print(result1)

customer = {
    'firstName': 'John',
    'lastName': 'Lennon',
    'weight' : 88,
    'height' : 1.76
}
query = customer['lastName']
print(query)
query2 = customer['height']
print(query2)

dic ={ 1: 55, 2:[10,20,30], 3: {'s1' : 100, 's2' : 200}}
print(dic[2])
print(dic[2][1]) #[key][index]
print(dic[3]['s2'])  #[key][innerkey]

dic = {'k1':['a','b','c'], 'k2' : ['d','e','f']}
print(dic['k2'][1].upper()) #to print e in capitals.
print(dic['k1'][1].upper())

dic = {1: 'a', 2: 'b'}
print(dic)
dic[3] = 'c' #add
print(dic)
dic[2] = 'B' #overwrite
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items()) #elements printed as tuples.


#Update multiple keys (usual way)
my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict["country"] = "Colombia"
my_dict['age'] = 36
my_dict['occupation'] ='Editor'
print(my_dict)


#Update multiple keys (one line)
my_dict.update({"country": "Colombia", "age": 36, "occupation": "Editor"})
print(my_dict)
