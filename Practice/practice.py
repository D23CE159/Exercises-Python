# 1 Reverse the given string
def reverse(string):
    reverseString = ""
    for char in string:
        reverseString = char + reverseString
    return reverseString

string = "Nehit"

print("Original String: ", string)
print("Reverse String: ", reverse(string))

# 2 Replace some character of the string with another character without using loop.
print(string.replace("e", "i"))

# 3 Find whether the character in the given string or not.
char = "N"
if char in string:
    print(string.index(char))

# 4 Create tuple, list and set and convert them into the different strings.
lst = ['N', 'e', 'h', 'i', 't']
tup = ('N', 'e', 'h', 'i', 't')
stringSet = set()
stringSet.add("N")
stringSet.add("e")
stringSet.add("h")
stringSet.add("i")
stringSet.add("t")

strLst = ""
strTup = ""
strSet = ""
for i in lst:
    strLst = strLst + i

for i in tup:
    strTup = strTup + i

for i in stringSet:
    strSet = strSet + i

print("List to String: ", strLst)
print("Tuple to String: ", strTup)
print("Set to String: ", strSet)

# 5 Convert all the string characters to the upper and the lower case and split it with the different methods.
print(string.upper())
print(string.lower())
print(string.split("h"))

# 6 Perform the following operations to the tuple and the list
numTup = (1, 10, 55, 5, 25)
print("Max in Tuple: ", max(numTup))
print("Min in Tuple: ", min(numTup))
print("Sum in Tuple: ", sum(numTup))
print("Length in Tuple: ", len(numTup))

numLst = [1, 2, 75]
print("Max in List: ", max(numLst))
print("Min in List: ", min(numLst))
print("Sum in List: ", sum(numLst))
print("Length in List: ", len(numLst))

# 7 Copy one list to the another list without using the copy command
newNumLst = numLst[:]
print(newNumLst)

# 8 Perform below task as instructed
"""
    Create a dictionary named student with 
    key: 'name', 'age', and 'grade'. Assign values accordingly.
    Access Dictionary Values:
"""
student = {
    'name': 'Nehit',
    'age': 20,
    'grade': 'AA',
}

for val in student.values():
    print(val)

""" 
    Print the 'age' of the student from the dictionary created in Exercise 1.
    Modify dictionary Values:
"""
print("Age of the student: ", student['age'])
student['name'] = "Nehit Vasavada"
student['grade'] = "AB"
for val in student.values():
    print(val)

"""
    Update the 'grade' of the student to a new value.
"""
student.update({'grade': 'AA'})
print(student)

"""
    Check if the key 'gender' is present in the student dictionary.
    Print a message based on the result.
"""
if 'gender' in student.keys():
    print("Gender is in the dictionary")
else:
    print("Gender key is not present in the dictionary")

# 9 perform below task as instructed
"""
    Create two sets: set1 with element(1, 2, 3) and set2 with elements(3, 4, 5)
    Union of Sets:
"""
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
print(set1)

set2 = set()
set2.add(3)
set2.add(4)
set2.add(5)
print(set2)

"""Find the union of set1 and set2 and print the result"""
print(set1.union(set2))

"""Find the intersection of set1 and set2 and print the result"""
print(set1.intersection(set2))

"""Find the elements that are in set1 but not in set2 and print the result"""
print(set1.difference(set2))
print(set2.difference(set1))

"""Check if set1 is a subset of set2. Print a message base on the result"""
if set1.issubset(set2):
    print("Yes, set1 is a subset of set2")
else:
    print("No, set1 is not a subset of set2")

# Perform below task as instructed
"""
    create a dictionary where keys are subjects ('maths', 'science') and 
    values are sets of students who take those subjects
"""
mathSubject = set()
mathSubject.add("Yash")
mathSubject.add("Kunj")
mathSubject.add("Nehit")
scienceSubject = set()
scienceSubject.add("Nehit")
scienceSubject.add("Rohit")
scienceSubject.add("Mahendra")

subjects = {
    'maths': mathSubject,
    'science': scienceSubject,
}

for key, value in subjects.items():
    print(key, ":", value)

"""
    Update set Values:
    Add a new student to the math subject in the dictionary from Exercise 11.
"""
mathSubject.add("Virat")
subjects.update({'maths': mathSubject})
for key, value in subjects.items():
    print(key, ":", value)

"""Remove a student from the 'science' subject in the dictionary from Exercise 11."""
scienceSubject.remove("Rohit")
for key, value in subjects.items():
    print(key, ":", value)

"""
    Check Common Students:
    Find and print the student who take both 'math' and 'science'.
"""
commonStudent = mathSubject.intersection(scienceSubject)
for key in subjects.keys():
    result = f"{commonStudent} take {key}"
    print(result)

"""
    create a nested dictionary where each key represents a country
    and the value is another dictionary containing cities and their populations.
"""

country = {
    "India": {
        "City": "Junagadh",
        "Population": "1.5M"
    },
    "Canada": {
        "City": "Ottawa",
        "Population": "880K"
    }
}

""" 
    11 create two lists, one containing elements at even indices
    and other containing elements at odd indices from the original list.
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenLst = []
oddLst = []

for i in lst:
    if i % 2 == 0:
        evenLst.append(i)
    else:
        oddLst.append(i)

print(evenLst)
print(oddLst)

# 12 Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.
a = 5
b = 6
tup = (a, b)
(b, a) = tup
print(a)
print(b)

# Check if a given list is a palindrome using slicing
def is_palindrome(lst):
    return lst == lst[::-1]

my_list = [1, 2, 3, 2, 1]
result = is_palindrome(my_list)

if result:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

# 14 concatenate two tuples without using the + operator
tup1 = (1, 2, 3, 4,)
tup2 = (5, 6, 7, 8,)
lst1 = list(tup1)
lst2 = list(tup2)
lst1.extend(lst2)
res = tuple(lst1)
print(res)

