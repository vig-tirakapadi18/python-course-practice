# Creation of dict
d = {1: "Vig", 2: "Hello", 3: "Hi", 4: "Hey"}

# Heterogeneous Data
d = {1: "vig", "two": "Hello", 3.234: 100, 6+7j: "Hey"}
print(d)

# Can't store duplicate keys
# It only prints last hey-value if duplicate keys are present
d = {1: "Hello", 1: "Hi", 1: "Vig"}
print(d)  # {1: 'Vig'}

# Storing duplicate values for different keys
d = {1: "ABC", 2: "ABC", 3: "ABC", 4: "ABC"}
print(d)

# dicts are Mutable
d = {}

d[5] = "Vighnesh"   # Updating dict - way 01
print(d)  # {5: 'Vighnesh'}

# Updating value - way 02
d.update({2: "Hello", 6: "Hi", "Hey": "How are you!"})
print(d)  # {5: 'Vighnesh', 2: 'Hello', 6: 'Hi'}

del d[2]
print(d)  # {5: 'Vighnesh', 6: 'Hi'}

# d.pop()  # TypeError: pop expected at least 1 argument, got 0

d.pop("Hey")
print(d)  # {5: 'Vighnesh', 6: 'Hi'}

d.popitem()  # Deletes the last key-value pair
print(d)  # {5: 'Vighnesh'}

d.clear()  # Clears the dict (Doesn't delete it)
print(d)  # {}

del d  # Deletes the whole dict
# print(d)  # NameError: name 'd' is not defined. Did you mean: 'id'?


# FETCHING keys or values or key-value
d = {1: "Hello", "Hey": "How are you doing!",
     3: 1.234567, 6+7j: True, False: "Haha"}

# KEYS
print("All KEYS: ")
for i in d.keys():
    print(i, end=" ")

print()
# VALUES
print("All VALUES: ")
for i in d.values():
    print(i, end=" ")

print()
# KEY-VALUE
print("All KEY_VALUE Pairs: ")
for i in d.items():
    print(i, end=" ")
