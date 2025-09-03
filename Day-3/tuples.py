#Tuples are just like list but immutable (Can't be changed)
#Can contain any datatypes.

#Adv of Tuples over lists:
#Less memory, so faster processing.
#Damage proof.

my_tuple = (1,2,3,4,5)
my_tuple2 = 1,2,3,4,5 #can be declared without parantheses as well.
print(my_tuple)
print(type(my_tuple))

t=(5, 5.6, 'fff')
print(my_tuple[0])
print(my_tuple[-2])
#my_tuple[0] = 4
#print(my_tuple) #Error - Tuple doesnt support item assignment.

my_tuple = (1,2,(10,20),5)
print(my_tuple[2][0]) #[index][inner_index]

my_tuple = list(my_tuple) #type casting
print(type(my_tuple))

my_tuple = tuple(my_tuple)  #back to tuple again.

t = (1,2,3)
x,y,z = t #multiple assignments
#x,y,z,a = t #ValueError
print(x,y,z)

print("---------------")
t=(1,2,3,1)
print(len(t))
print(t.count(1))
print(t.index(2)) #what is the index of 2? -> 1