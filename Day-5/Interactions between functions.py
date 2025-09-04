# Pick a stick game.
from random import shuffle


# initial list
sticks = ['-','--','---','----']

# mixing sticks
def mix(my_list):
    shuffle(my_list)
    return(my_list)

print(mix(sticks))

# choose number
def try_your_luck():
    a_try = ''
    while a_try not in ['1','2','3','4']: #to make sure the number they pick is not number or letter, but a number between 1 and 4.
        a_try = input('Choose a number: ')

    return int(a_try)
#try1 = try_your_luck()
#print(try1)


# check players try
def verify_try(a_list, a_try): #these are internal variables only
    if a_list[a_try - 1] == '-':
        print("Wash the dishes")
    else:
        print("This time you are safe")

    print(f"You got {a_list[a_try - 1]}")

mixed_sticks = mix(sticks)
selection = try_your_luck()
verify_try(mixed_sticks, selection) #The order of functions is also important


