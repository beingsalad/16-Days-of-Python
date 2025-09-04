def greet_person():
    '''
    This function is used to greet people  (good practice)
    another line.
    '''
    # this function is good for something
    print("Hello") #running this will give no output. We didn't call the function yet.

greet_person()    #execute the function and do everything inside it.

# passing parameters (information the function receives at the moment being called)
def greet_person2(name):
    print("Hello " + name) #the value of name will loaded at the moment of calling this function.

greet_person2("frank") #Definition of this function needs a parameter now.
greet_person2("Deepak")

#This becomes reusable for many parameters which might be changing in the future.
def welcome(name):
    print(f"Welcome {name}!")