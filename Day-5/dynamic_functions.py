# # Create a function that is in charge of checking
# # def check_3_digit1(number):
# #     return number in range(100,1000) #checks from 100 to 999.
# #
# # result = check_3_digit1(68)
# # print(result)
#
# # More complexity
# # def check_3_digit2(number):
# #     return number in range(100,1000) #checks from 100 to 999.
# #
# # sum = 526 + 311
# # result = check_3_digit2(sum)
# # print(result)
#
#
# # Create a function to check three digits to do the same.
# # It actually does.
# # But instead of checking a single number to check all the numbers from a list and returns true if at
# # least one of those numbers has three digits.
# def check_3_digit4(list1):
#     for num in list1:
#         if num in range(100,1000):
#             return True #Once we find the first 3 digit number, it will return true and exit the function immediately.
#         else:
#             pass
#
# result = check_3_digit4([45,23,4569]) #function didnt return anything, but it has to return something. right? So, we got an empty object - None.
# print(result)
#
# result1 = check_3_digit4([455,23,4569]) #the loop will end with number 455 itself. It wont even go to the other 2 numbers
# print(result1)
#
# result3 = check_3_digit4([55,23,609])
# print(result3)
#
# #what if you want to print False if you dont have a three digit number?
# def check_3_digit5(list2):
#     for num in list2:
#         if num in range(100,1000):
#             return True
#         else:
#             return False
#
# result4 = check_3_digit5([55,23,609]) #It gives False. Because for the first number, it returns false. So, it exits the loop immediately even though i had a 3 digit number at the last.
# print(result4)
#
# # First number in [55, 23, 609] is 55.
# # 55 in range(100,1000) → False.
# # So it hits the else: return False immediately → function exits.
# # It never checks 23 or 609.
# # ✅ Problem: It decides True/False on the first element only.
#
#
#
# def check_3_digit6(list2):
#     for num in list2:
#         if num in range(100,1000):
#             return True
#         else:
#             pass
#     return False
#
# result5 = check_3_digit5([55,23,609])
# print(result5)
#
# # First number 55 → not in range → just pass (does nothing).
# # Moves on to next number 23 → still not in range → pass.
# # Moves on to next number 609 → in range → returns True.
# # If it finishes the loop with no matches, it finally returns False.
# # ✅ Correct logic: It keeps checking until it finds a 3-digit number.
#
#
# I want the function to print a list with all 3 numbers.
list_bools = []
def check_3_digit7(list3):
    for num in list3:
        if num in range(100,1000):
            list_bools.append("True")
        else:
            list_bools.append("False")
    return list_bools

result6 = check_3_digit7([553,23,609])
print(result6)



def check_3_digit8(list3):

    three_digit_list = [] #not a global variable

    for num in list3:
        if num in range(100,1000):
            three_digit_list.append(num)
        else:
            pass
    return three_digit_list

result7 = check_3_digit8([553,23,609])
print(result7)


# return:
# Exits the entire function immediately.
# Sends a value back to the caller (or None if no value is given).
# No further code in that function is executed.

# break:
# Exits only the innermost loop, not the function.
# Execution continues after the loop.

# pass:
# Does nothing.
# It is just a placeholder to keep code syntactically valid.

# Exercise1:
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative.
# Create a list named numbers with positive and negative values.
def all_positives(list):
    for n in list:
        if n <= 0:
            return False
        else:
            pass
    return True

numbers1 = [4, 3, 2, 1, 1, 2, 3, 4, 5] #Give 0 here. You will get False.
result8 = print(all_positives(numbers1))

# Exercise2:
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
def sum_less(list):
    total = 0
    for num in list:
        if 0 < num < 1000:
            total = total + num
        else:
            pass
    return total
numbers = [1022,2,56,70000,3,12,3]
print(sum_less(numbers))

# Exercise3:
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even(list):
    count = 0
    for n in list:
        if n % 2 == 0:
            count = count + 1
        else:
            pass
    return count

numbers = [2, 4, 5, 6, 7, 8, 8]
print(count_even(numbers))