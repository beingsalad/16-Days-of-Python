# Match looks for coincidences
# Match is used for structural pattern matching.
series = 'N-02'

# Logic with normal if-elif-else condition.
'''if series == "N-01":
    print("Samsung")
elif series == "N-02":
    print("Nokia")
elif series == "N-03":
    print("Motorola")
else:
    print("This product doesn't exist")'''

#Match (python 3.10)
match series:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("This product doesn't exist")

client = {'name': "Federico",
         'age': 46,
         'occupation':'instructor'} #3 elements
movie = {'title': 'Matrix',
         'credits': {'main_star':'Keanu Reeves',
                    'director':'Lana & Lilly Wachowski'}} #2 elements and credits with 2 more elements.

items = [client, movie,'book']

for i in items: #for element in items
    match i:
        case {'name': name, #in the case if it coincides with this structure.
              'age': age,
              'occupation': occupation}:
            print("It is a client")
            print(name, age, occupation) #'name' means: the dictionary must have a key "name".
                                         #name (no quotes) means: take the corresponding value and store it in a variable called name.
        case {'title': title,
              'credits':{'main_star': main_star,
                         'director': director}}:
            print("It is a movie")
            print(title, main_star, director)
        case _:
            print("I don't know what it is")