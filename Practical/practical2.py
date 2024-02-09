# Practical 2

# (A)Create a list and apply methods(append, extend, remove, reverse), arrange created list into the ascending and descending order
print("Practical 2 - A")
friends = ['nehit', 'yash', 'navdeep', 'kunj']
friends.append('amit')
print(friends)
friends.reverse()
print(friends)
friends.remove('kunj')
print(friends)
friends.extend(['shees'])
print(friends)
print(sorted(friends))
print(friends)
friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)

# (B)
print("\nPractical 2 - B")
List1 = [1, 2, 3, 4, ['python', 'java', 'c++',[10, 20, 30]], 5, 6, 7, ['apple', 'banana', 'orange']]

values = List1[4][0:1] + List1[8][2:3]
five_values = [values] * 5
print(five_values)

# (C)
print("\nPractical 2 - C")
cars = ['lamborghini', 'audi', 'mg', 'scorpio', 'mustang']
duplicate_cars = cars[:]
print(duplicate_cars)

# (D)
print("\nPractical 2 - D")
numbers = (3, 7, 1, 50, 20)
print(max(numbers))
print(min(numbers))
print(sum(numbers))