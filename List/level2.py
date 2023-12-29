# Exercise Level 2

ages = [19, 22, 19, 24, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print(max(ages))
print(min(ages))

# Add the min age and the max age again to the list
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

# Find the median age (one middle item or two middle items divided by two)
middle_age = len(ages) // 2
print(middle_age)

# Find the average age(sum of all items divided by their number)
sum_of_age = sum(ages)
print(sum_of_age)
avg = sum_of_age / len(ages)
print(avg)

# Find the range of the ages (max minus min)
range_of_age = max(ages) - min(ages)
print(range_of_age)

# Compare the value of (min - average) and (max - average), use abs() method
min_abs = abs(min_age - avg)
max_abs = abs(max_age - avg)
if min_abs < max_abs:
    print("The difference is less")
elif min_abs > max_abs:
    print("The difference is high")
else:
    print("Equal")

# Find the middle country(ies) in the [countries list]
countries = ['India', 'Australia', 'Canada', 'New Zealand', 'America']
middle_country = len(countries) // 2
print(countries[middle_country])

"""Divide the countries list into two equal lists if it is even if not
one more country for the first half"""
if len(countries) % 2 == 0:
    first_half = countries[ : middle_country]
    second_half = countries[middle_country : ]
    print(first_half)
    print(second_half)
else:
    first_half = countries[ : middle_country + 1]
    second_half = countries[middle_country + 1 : ]
    print(first_half)
    print(second_half)

"""['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
Unpack the first three countries and the rest as scandic countries."""
country_names = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *rest = country_names
print(first_country)
print(second_country)
print(third_country)
print(rest)