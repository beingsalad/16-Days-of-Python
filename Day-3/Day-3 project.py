'''You are going to create a program that first asks the user to
enter text. It can be any text, an entire article, a paragraph, a sentence, a poem,
whatever you want. Then the program will ask the user to enter three random letters.
From that moment on, our code is going to process that information and result in five
different types of analysis:

1. How many times each of those letters they have chosen appears. To achieve this, I
advise you to store those letters in a list, and then use a method of strings that allows
you to count how many times a substring appears within the string. One thing to keep
in mind is that when searching for letters, there can be upper and lower case and this
will affect the result. So, to make sure that absolutely all letters are counted, you should
pass both the original text and the letters to be searched to lowercase.

2. How many words are in the whole text? To achieve this part, remember that there is
a string method that allows us to transform it into a list. And then there is a function
that allows us to find out the length of a list.

3. What are the first and last letters of the text? Here, we will clearly use indexing.

4. The system will show us how the text would look like if we inverted the order of the
words. Is there any method that allows us to invert the order of a list? And another one
that allows us to join these elements with spaces in between?

5. The system will tell us if the word “python” is inside the text. This part can be a bit
complicated to imagine, but I'll give you a hint: you can use Booleans to make your
enquiry and a dictionary to find ways to express your answer. '''

# text = ('''My name is Deepak. I am an Analyst working in a company named Proclink Consultancy Services. Its a huge company with more than 200 employees and with dozen of domain people working together towards one goal, which is performance through innovation''')
# letters = input("Enter 3 random letters: ")
# letters_list = list(letters)
# print(letters_list)
#
# #Counting the number of times the letters appear in the paragraph.
# result1 = text.count(letters_list[0])
# print(result1)
#
# #how many words
# words = text.split(" ") # split by spaces, returns a list
# print(words)
# length = len(words)
# print(f"The length of the list is: {length}")
#
# #first and last letters of the text
# first = text[0]
# last = text[-1]
# print(f"The first letter of the list is: {first} and the last letter of the list is: {last}")
#
# #inverted order
# #invert = words[::-1]
# invert = words.reverse()
# print(words) #inplace method.
# joined = " ".join(words)
# print(joined)
#
# #if python is there in the text
# isthere = "Python" in text
# print(isthere)
#
# print("---")

#Tutor solution
text = input("Enter the text of your choice: ")
letters = []

text = text.lower()

letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the third letter: ").lower())

print("\n") #linebreak
print("LETTER REPETITIONS")

letter_repetitions1 = text.count(letters[0])
letter_repetitions2 = text.count(letters[1])
letter_repetitions3 = text.count(letters[2])

print(f"We have found the letter {letters[0]} repeated {letter_repetitions1} times")
print(f"We have found the letter {letters[1]} repeated {letter_repetitions2} times")
print(f"We have found the letter {letters[2]} repeated {letter_repetitions3} times")

print("\n") #linebreak
#Number of words in the text
print("NUMBER OF WORDS")

words = text.split(" ")
print(f"we have found {len(words)} words")

print("\n") #linebreak
print("FIRST AND LAST LETTERS")
first_letter = text[0]
last_letter = text[-1]
print(f"The first letter of the list is:'{first_letter}' and the last letter of the list is:'{last_letter}'")

print("\n")
print("INVERTED TEXT")
words.reverse() #in-place method.
inverted_text = " ".join(words)
print(f"If we order your text backwards it will say '{inverted_text}'")

print("\n")
print("LOOKING FOR THE WORD PYTHON")
is_python = 'python' in text
dic = {True : 'was', False: 'was not'}
print(f"The word 'Python' {dic[is_python]} found in the text")
