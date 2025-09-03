x = 10
y = 5

#Method 1
print("My numbers are " + str(x) + " and " + str(y)) #Usual method - too much work.

#Method 2
print("My numbers are {} and {}".format(x, y))
print("My numbers are {} and {}".format(y, x))

print("My sum of {} and {} is equal to {}".format(x, y, y+x))

#Method 3
color = "red"
license_plate = 541926

print(f"The car is {color} and its license plate is {license_plate}")
#putting a f in front of the " is like telling python that "Listen python, this is going to be a literal string"