# Sets can be declared in 2 ways.
# One way is to declare values inside {} (Only values. Or else it will become a dictionary xD)
# 2nd way is to use the set keyword. set(1,2,3,4,5). One drawback is if we create a set using the set keyword and paratheses, it will take a single argument only.
# We know list can take different datatypes. But here, you can't include dictionary and another list to it.

# They dont contain duplicate values. Sets are unordered.
my_set = set([1,2,3,4,5]) #within a set, we should include a single argument.
print(type(my_set))
print(my_set)

other_set = {1,2,3}
print(type(other_set))
print(other_set)
#print(my_set[0]) #unordered, not subscriptable.
#my_set[0] = 5 #doesnt support item assignment.

my_set = set((1,2,3,4,5,2,3,1,2,3,5,))
#my_set = set((1,2,3,4,[5,2],3,1,2,3,5,)) #error.
my_set = set((1,2,3,4,5,(2,3,1,2),3,5,)) #since tuples are immutable, this is an exception.
print(my_set)
print(len(my_set))
print(2 in my_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
print(s1)
s1.add(2)
print(s1) #doesnt add duplicate values.
s1.remove(3)
print(s1)
s1.discard(6)
print(s1)

draw = s1.pop()
print(draw)
s1.clear() #empty that set.
print(s1)

#Sets support strings, tuples, floats, integers but not lists (mutable objects).


