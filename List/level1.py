# Exercise Lever 1

# 1 Declare an empty List
empty_list = []

# 2 Declare a list with more than 5 items
list_of_items = [1, 2, 3, 4, 5]

# 3 Find the length of your list
length = len(list_of_items)
print(length)

# 4 Get the first item, the middle item and the last item of the list
print(list_of_items[0])
middle_item = length//2
print(list_of_items[middle_item])
print(list_of_items[-1])

"""5 Declare a list called mixed_data_types, put your(name, age, height,
marital status, address)"""
mixed_data_types = ['nehit', 19, 5.7, False, 'Anand']

"""6 Declare a list variable named it_companies and assign 
initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon"""
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 Print the list using print()
print(it_companies)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
middle_company = len(it_companies)//2
print(it_companies[0])
print(it_companies[middle_company])
print(it_companies[-1])

# 10 Print the list after modifying one of the companies
it_companies[middle_company] = 'Infosys'
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append('Apple')
print(it_companies)

# 12Insert an IT company in the middle of the companies list
middle_company = len(it_companies)//2
it_companies.insert(middle_company, 'TCS')
print(it_companies)

# 13 Change one of the it_companies names to uppercase(IBM excluded!)
print(it_companies[1].upper())

# 14 Join the it_companies with a sting '#; '
join_string = '#; '.join(it_companies)
print(join_string)

# 15 Check if a certain company exists in the it_companies list.
if 'IBM' in it_companies:
    print("IBM is exist in the list.")
if 'HCL' in it_companies:
    print("HCL is in the list.")
elif 'HCL' not in it_companies:
    print("HCL is not in the list")

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18 Slice our the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)

# 19 Slice our the last 3 companies from the list
last_three_companies = it_companies[6:]
print(last_three_companies)

# 20 Slice our the middle IT company or companies from the list
middle_three_companies = it_companies[3:6]
print(middle_three_companies)

# 21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22 Remove the last middle IT company from the list
middle_company = len(it_companies)//2
it_companies.pop(middle_company)
print(it_companies)

# 23 Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 Destroy the IT company list
del it_companies

# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_back_end = front_end + back_end
print(front_back_end)

""" 27 Copy the joined list and assign it to a variable full_stack.
Then insert Python and SQL after Redux."""
full_stack = front_back_end[:]
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)