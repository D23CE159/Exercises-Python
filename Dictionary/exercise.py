# Exercises - Dictonary

# 1 Create an empty dictionary called dog
empty_dictionary = {}
print(empty_dictionary)

# 2 Add name, color, breed, legs, age to the dog dictionary
dog_dictionary = {
    'name' : 'Murfy',
    'color' : 'Golden',
    'breed' : 'Labrador retriever',
    'legs' : 4,
    'age' : 2,
}

for info, details in dog_dictionary.items():
    print(f"{info.title()} : {details}")

"""3 Create a student dictionary and add first_name, last_name, gender, age,
marital status, skills, country, city and address as keys for the dictionary"""
student = {
    'first_name' : 'Nehit',
    'last_name' : 'Vasavada',
    'gender' : 'Male',
    'age' : 19,
    'marital status' : 'unmarried',
    'skills' : ['fast touch typing', 'cricket'],
    'country' : 'india',
    'city' : 'junagadh',
    'address' : 'anand',
}

# 4 Get the length of the student dictionary
length = len(student)
print(length)

# 5 Get the value of skills and check the data type, it should be a list
skills = student['skills']
data_type = type(skills)
print(data_type)

# 6 Modify the skills values by adding one or two skills
modify_skill = student['skills'].append('gaming')
for value in student['skills']:
    print(value)
print(student)

# 7 Get the dictionary keys as a List
list_keys = list(student.keys())
print(list_keys)

# 8 Get the dictionary values as a list
list_values = list(student.values())
print(list_values)

# 9 Change the dictionary to a list of tuples using items() method
tuple_student = student.items()
print(tuple_student)

# 10 Delete one of the items in the dictionary
deleted_item = student.pop('age')
print(deleted_item)
print(student)

# 11 Delete one of the dictionaries
del student
print(student)
