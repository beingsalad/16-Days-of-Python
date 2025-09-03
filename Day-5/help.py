dic ={'key1':100,
      'key2':200,
      'key3':300,
      'key4':400}

a = dic.popitem() #click the middle of the () and hold your cursor for a while.
print(a) #After an object and putting a dot, you will get a lot of suggestions on methods, class, properties.
print(dic)

# Exercise1
text = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#".lstrip(",:%_#")
print(text)

# Exercise2
fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3,"Orange")
print(fruits)

# Exercise 3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method
phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}
isolated_sets = phone_brands.isdisjoint(tv_brands)