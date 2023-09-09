# Creating strings
str = "Hello"

str = 'Hello'

str = '''Hello Vighnesh!'''

str = """Hello Vighnesh!"""


# Built-in Methods
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())


# split()
str = "Hel looo Vig hnes h!"
print(str.split())
print(str.split("o"))
# print(str.split(""))    #ValueError: empty separator


# WAPP to take a list of elements from user
# WAY - 1
'''li = []

n = int(input("How many elements you want to store? "))

for i in range(0, n):
    i = int(input("Enter an el: "))
    li.append(i)

print(li)'''


# WAY - 2
'''lst = input("Enter comma(,) seperated elements: ")

new_lst = lst.split(",")
print(new_lst)'''


# id()
print(id(str))
print(id(str[2]))
print(id(str[4]))
print(id(str[5]))
print(id(str[6]))
print(id(str[7]))


# Comparison Operator in Strings
# CASE - 1
s1 = "vighnesh"
s2 = "vighnesh"

if s1 == s2:
    print("Values are Equal!")
else:
    print("Values are not Equal!")

if id(s1) == id(s2):
    print("Address are Equal!")
else:
    print("Address are Not Equal!")

# CASE - 2
s1 = "vighnesh"
s2 = "VIGHNESH"

if s1 == s2:
    print("Values are Equal!")
else:
    print("Values are not Equal!")

if id(s1) == id(s2):
    print("Address are Equal!")
else:
    print("Address are not Equal!")

# CASE - 3
s1 = "VIGHNESH"
s2 = "vighnesh"

s2 = s2.upper()

if s1 == s2:
    print("Values are Equal!")
else:
    print("Values are not Equal!")

if id(s1) == id(s2):
    print("Address are Equal!")
else:
    print("Address are not Equal!")
