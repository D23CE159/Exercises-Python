# Exercise Level 1

# 1 Create an Empty Tuple
empty_tuple = ()
print(empty_tuple)

""" 2 create a tuple containing names of your sisters and your brothers(imaginary
siblings are fine)"""
sisters = ('Deepika', 'Sara', 'karina', 'Priyanka', 'Mrunal')
brothers = ('Dhoni', 'Rohit', 'Ravindra', 'Shikhar', 'Raina')
print(sisters)
print(brothers)

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# 4 How many siblings do you have?
print(len(siblings))

"""5 Modify the siblings tuple and add the name of your father and mother 
and assign it to family_members"""
father_mother = ('Shiv', 'Shakti')
family_members = siblings + father_mother
print(family_members)

# Exercise Level 2

# 1 Unpack siblings and parents from family_members
unpacking = father_mother, *siblings
print(unpacking)
print(father_mother)
print(siblings)

"""2 create fruits, vegetables and animal products tuples. join the three
tuples & assign it to a variable called food_stuff_tp"""
fruits = ('apple', 'banana', 'orange', 'guava', 'pear')
vegetables = ('carrot', 'tomato', 'potato', 'bottle gourd', 'Lady finger')
animals = ('dog', 'cat', 'lion', 'tiger', 'wolf')
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4 Slice out the middle item or items from the food_stuff_tp or food_stuff_lt list
middle_tuple = len(food_stuff_tp) // 2
print(food_stuff_tp[middle_tuple])
middle_list = len(food_stuff_lt) // 2
print(food_stuff_lt[middle_list])

# 5 Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

# 6 Delete the food_staff_tp tuple completely
del food_stuff_tp
print(food_stuff_tp)

# 7 Check if an item exists in tuple
if 'lion' in food_stuff_tp:
    print("Lion is in the Tuple")

# 8 Check if 'Estonia' is a nordic country
nordic_country = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_country:
    print(True)
else:
    print(False)

# 9 Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_country:
    print(True)
else:
    print(False)
