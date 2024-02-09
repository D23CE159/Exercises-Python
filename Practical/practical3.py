# A String Operations:

# Reverse a String
def reverse(string):
    newString = ""
    for char in string:
        newString = char + newString
    return newString

string = "Nehit"
print("Original String: ", string)
print("Reverse String: ", reverse(string))

# Replace String with other String
print("Replacing the string: ", string.replace("Ne", "Mo"))

# merge two string
string1 = "Vasavada"
str = string + " " + string1
print(str)

# Find character is in string or not without using loops
print("hi" in str)

# Split string into multiple words and characters
print(str.split())

# B Dictionary Operations:
# Apply "update, delete, clear, popitem, pop, get, keys and values" operation in dictionary
country = {
    "city": "Junagadh",
    "population": "1.5M",
}

country.update({"mountain": "Girnar"})

for key, value in country.items():
    print(f"{key}: {value}")



del country["population"]
print(country)

key = country.keys()
print(key)
val = country.values()
print(val)

popElement = country.pop("mountain")
print(popElement)

popItem = country.popitem()
print(country)

country.update({"mountain": "Girnar"})
country.update({"city": "Junagadh"})

country.clear()
print(country)

# Create 3 dictionaries and merge them into dictionary

def Merge (dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {
    "City": "Junagadh",
    "population": "1.5M",
}

dict2 = {
    "mountain": "Girnar",
    "famous place": "bhavnath",
}

dict = Merge(dict1, dict2)
print(dict)
