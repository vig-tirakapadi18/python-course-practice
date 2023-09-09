# Creation of Tuple
tup = (10, 20, 30, 40, 50)

# type of Tuple
print(type(tup))  # <class 'tuple'>

# Heterogeneous Data
tup = (10, 20, "Vighnesh", "V", 6+7j, False)

# Duplicate values
tup = (10, 20, 30, 20, 10, 30, 40, 50, 90, 60, 40)
print(tup)

# tup[2] = 200    #TypeError: 'tuple' object does not support item assignment

# tup.remove(30)  #AttributeError: 'tuple' object has no attribute 'remove'

# tup.pop(2)  #AttributeError: 'tuple' object has no attribute 'pop'

tup = (10)  # Not singleton tuple
tup = (22,)  # Singleton tuple
