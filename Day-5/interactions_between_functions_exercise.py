# Exercise1

# Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).
# Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:
# If the sum is less than or equal to 6:
# "The sum of your dice is {sum_dice}. Unfortunate"
# If the sum is greater than 6 and less than 10:
# "The sum of your dice is {sum_dice}. You have a good chance"
# If the sum is greater than or equal to 10:
# "The sum of your dice is {sum_dice}. It looks like a winning roll"

# Rolling two random dice and returning something based on the sum of the rolls.
# from random import randint
#
# def throw_dice():
#     dice1 = randint(1,6)
#     dice2 = randint(1,6)
#     return dice1,dice2
#
# def roll_result(dice1,dice2):
#     sum_dice = dice1 + dice2
#     if sum_dice <= 6:
#         return (f"The sum of your dice is {sum_dice}. Unfortunate")
#     elif sum_dice > 6 and sum_dice < 10:
#         return (f"The sum of your dice is {sum_dice}. You have a good chance")
#     elif sum_dice >= 10:
#         return (f"The sum of your dice is {sum_dice}. It looks like a winning roll")
#     else:
#         pass
#
# d1, d2 = throw_dice()
# print(f"You rolled {d1} and {d2}")
# print(roll_result(d1, d2))


# Exercise 2:
# Interactions Between Functions Practice #2
# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the elements can be changed.
# For example, if given the list [1,2,15,7,2] it should return [1,2,7].
# Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values.

# def reduce_list(my_list):
#     '''
#     Function that takes a list as an argument.
#     Returns also a list, but removing duplicates and removing the highest value.
#     '''
#     unique_list = list(set(my_list))
#     maximum = max(unique_list)
#     updated_list =[]
#     for i in numbers:
#         if i < maximum:
#             updated_list.append(i)
#         else:
#             pass
#     return updated_list
#
# numbers = [2,3,4,14,2]
# print(reduce_list(numbers))
#
# def average(updated_list):
#     avg = sum(updated_list) / len(updated_list)
#     return avg
#
# print(average(numbers))



# Exercise3:
# You must create a list with values and call it secret_codes.
# Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.
# Create a second function called luck, that takes two arguments: the first must be the result of the coin toss. The second argument will be any list (the secret_codes variable that was created at the beginning).
# If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ].
# If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.

from random import choice          # import only choice for clarity

secret_codes = [23, 45, 1, 23, 112, 456]   # sample list

# Function to simulate a coin toss
def toss_coin():
    toss = ["Heads", "Tails"]      # possible outcomes
    my_random = choice(toss)       # randomly pick one value from the list
    return my_random               # return the result ("Heads" or "Tails")

# Function that decides the fate of the list based on the toss result
def luck(my_random, my_list):
    empty_list = []                           # create an empty list if "Tails" happens
    if my_random == "Tails":                  # check if the toss was "Tails"
        print("List will self-destruct")      # message to the user
        return empty_list                     # return an empty list (list is "destroyed")
    else:                                     # otherwise, if toss was "Heads"
        print("List was saved")               # message to the user
        return my_list                        # return the original list

# Run the game
toss_result = toss_coin()                     # simulate a coin toss
print("Toss result:", toss_result)

final_list = luck(toss_result, secret_codes)  # pass toss result and list to luck()
print("Returned list:", final_list)

