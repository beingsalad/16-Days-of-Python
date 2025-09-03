my_bool = 4 < 5 < 6
print(my_bool)
my_bool2 = 4 < 5 > 6
print(my_bool2)

my_bool3 = 4 < 5 and 5 > 6 #AND - True, only if both conditions are True.
print(my_bool3)
my_bool4 = (4 < 5) or (5 == 2 + 3)
print(my_bool4)
my_bool5 = (55 == 55) or ('dog' == 'dog')
print(my_bool5)

my_bool6 = (4 > 5) or (5 == 2 + 3) #OR - True, if any one of the condition is True.
print(my_bool6)
my_bool7 = (4 > 5) or (5 == 5 + 3) #False, since both conditions aren't met.
print(my_bool7)

text = "This sentence is short"
my_bool8 = ("sentence" in text) and ('python' in text)
print(my_bool8)

my_bool9 = not 'a' != 'a' #NOT - Returns the opposite.
print(my_bool9)