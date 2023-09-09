# Creation of list
li = [10, 20, 30, 40, 50]

# Heterogeneous values
li = [10, 6+7j, True, "vighnesh", "V"]

# Duplicate values
li = [10, 20, 30, 10, 40, 30, 20, 60]

# type of list
print(type(li))  # <class 'list'>

# OPERATIONS ON LISTS
li = [100, 200, 300, 400, 500, 600, 700, 800, 900]
li[4] = 777  # Replaces the element at 4th position with new element
print(li)  # [100, 200, 300, 400, 777, 600, 700, 800, 900]

li.append(999)  # Adds element at the end
print(li)  # [100, 200, 300, 400, 777, 600, 700, 800, 900, 999]

li.remove(800)  # Removes a specified element
print(li)  # [100, 200, 300, 400, 777, 600, 700, 900, 999]

li.pop(3)  # Removes an element at specified position
print(li)  # [100, 200, 300, 777, 600, 700, 900, 999]

li.pop()  # Without index - Removes last element
print(li)  # [100, 200, 300, 777, 600, 700, 900]

del li[6]  # Deletes a specific data
print(li)  # [100, 200, 300, 777, 600, 700]

del li  # Deletes an entire list
# print(li)  # NameError: name 'li' is not defined

li = [100, 300, 222, 243, 123, 564, 432, 900, 888, 765, 564]
# sorted_li = sorted(li)  # Sorts list in ascending order
# print(sorted_li)  # [100, 123, 222, 243, 300, 432, 564, 564, 765, 888, 900]

li.sort()  # Also sorts the elements in ascending order
print(li)  # [100, 123, 222, 243, 300, 432, 564, 564, 765, 888, 900]

li.sort(reverse=True)  # Sorts in descending order
print(li)  # [900, 888, 765, 564, 564, 432, 300, 243, 222, 123, 100]

# "in" and "not in" - Checks if an element is present in list or not
print(500 in li)  # False
print(888 in li)  # True
print(999 not in li)  # True
