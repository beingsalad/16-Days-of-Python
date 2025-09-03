from multiprocessing.forkserver import read_signed
from xml.etree.ElementPath import prepare_self

my_text = "This text is a test"
result1 = my_text[7] #retriving a character from a certain index.
result2 = my_text[-3]
print(result1)
print(result2)

result3 = my_text.index("h") #finding the position of the string.
#result4 = my_text.find("q") #throws a ValueError.
result5 = my_text.index("test") #index where the substring starts.
print(result3)
#print(result4)
print(result5)

result6 = my_text.index("s") #retrives the first "s" in the string. Index searches from left to right.
print(result6)
result7 = my_text.index("s",5)  # the second parameter tells python from which index to start the search.
print(result7)
result8 = my_text.index("s",5,16)
print(result8)

result9 = my_text.rindex("s") #this method allows to search from right to left (searches backwards) but the index value will always be from left to right.
print(result9)

#Index method searches string from left to right. Index number is also from left to right.
#Rindex method searches string from right to left but the index number is from left to right.