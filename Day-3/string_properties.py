#Strings are immutable
name = "Harry"

name.replace("H","G")
#name[0] = "G" #error - string doesnt support item assignment.
#strings are immutable.
print(name) #when you print name, it says "Harry" ; not "Garry.

new_name = name.replace("H","G")
print(new_name) #Variables can vary. Strings can't.


#Concatenation
n1 = "Ga"
n2 = "rry"

print(n1 + n2) #concat

#Multiply
n1 = "Ga"
n2 = "rry"

print(n1 * 10)

#Line breaks in a string -> """   """, '''   '''
poem = """Thousand little white fish
as if boiled 
    the color of the water"""

print(poem)

#check if a certain word exist in a string
print("water" in poem) #Boolean
print("sun" in poem)
print("water" not in poem)
