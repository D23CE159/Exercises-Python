# A) Function to determine the grade based on SGPA
def find_grade(sgpa):
    if sgpa >= 9.0:
        return 'S'
    elif sgpa >= 8.0:
        return 'A'
    elif sgpa >= 7.0:
        return 'B'
    elif sgpa >= 6.0:
        return 'C'
    elif sgpa >= 5.0:
        return 'D'
    else:
        return 'F'

sgpa = float(input("Enter SGPA: "))
print("Grade:", find_grade(sgpa))


# B) Function to find the maximum from three numbers
def find_max(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("Maximum number is:", find_max(num1, num2, num3))


# C) Function to calculate the number of uppercase and lowercase letters in a string
def count_case(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return uppercase_count, lowercase_count

user_string = input("Enter a string: ")
upper, lower = count_case(user_string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# D) Function to find the square of a given list using a lambda function
square_list = lambda lst: [x**2 for x in lst]

given_list = [1, 2, 3, 4, 5]
print("Squared list:", square_list(given_list))


# E) Function to print the multiplication table
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number: "))
print_multiplication_table(num)


# F) Function to create a list from user-given values and calculate the sum using a loop
def sum_of_list():
    user_list = []
    n = int(input("Enter number of elements: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        user_list.append(element)
    return sum(user_list)

print("Sum of the list:", sum_of_list())


# G) Using list comprehension

# Separate lists of even and odd numbers from 1 to 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
odd_numbers = [num for num in range(1, 51) if num % 2 != 0]

# Values which are divisible by 5 from 1 to 100
divisible_by_5 = [num for num in range(1, 101) if num % 5 == 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Numbers divisible by 5:", divisible_by_5)

