text = "We are going to learn six methods today"
result = text
print(result)

result2 = text.upper()
print(result2)

result3 = text[4].upper()
print(result3)

result4 = text.lower()
print(result4)

result5 = text.split() #split the strings and store them in a list.
print(result5)

result6 = text.split('o') #split exactly at the string 'o'
print(result6)

a = "learning"
b = "Python"
c = "is"
d = "amazing"
e = " ".join([a,b,c,d]) #join all the elements we mention and it will seperate them with a space (as we mentioned here).
#We need to give the elements as a list only, as a parameter
print(e)
f = "-".join([a,b,c,d]) # a very weird method.
print(f)

result7 = text.find("s")
print(result7)

result8 = text.replace("six","a lot of")
print(result8)

result9 = text.replace("a","x")
print(result9)

#2 replace methods combined.
text = "If the implementation is hard to explain, it might be a bad idea."

print(text.replace("hard","easy").replace("bad","good"))