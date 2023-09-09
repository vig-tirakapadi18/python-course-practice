# Creation of set
s = {1, 2, 3, 4, 5}

# Heterogeneous data
s = {"Vighnesh", "V", 6+7j, 1.2345, 1000}
print(type(s))  # <class 'set'>

s = {10, 20, 30, 40, 50}

s.add(111)  # Adds element to a set
print(s)  # {50, 20, 40, 10, 30, 111}

s.remove(20)  # Removes element from a set
print(s)  # {50, 40, 10, 30, 111}

s.pop()  # removes first element from a set
print(s)  # {40, 10, 30, 111}

# s.pop(2)  # TypeError: set.pop() takes no arguments (1 given)

# del s[2]  # TypeError: 'set' object doesn't support item deletion

del s  # deletes the whole set
print(s)  # NameError: name 's' is not defined
