# Syntax :-
# new_list = [Expression for item in iterable if Condition]


# Example 1 - Copying list using List Comprehension
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 13, 14, 15]
copy_li = [i for i in li]
print(copy_li)


# Example 2 - Square of list items using List Comprehension
sq_li = [i**2 for i in li]
print(sq_li)


# Example 3 - Cube of list items using List Comprehension
cube_li = [i**3 for i in li]
print(cube_li)


# Example 4 - Power 4 of list items using List Comprehension
pow_4_li = [i**4 for i in li]
print(pow_4_li)


# Example 5 - Power 5 of list items using List Comprehension
pow_5_li = [i**5 for i in li]
print(pow_5_li)


# Example 6 - Even numbers of list using List Comprehension
even_li = [i for i in li if i % 2 == 0]
print(even_li)


# Example 7 - Odd numbers of list using List Comprehension
odd_li = [i for i in li if i % 2 != 0]
print(odd_li)


# Example 8 - Sample i/p = [1, 2, 3, 4, 5]  Sample o/p = [(1,1), (2, 4), (3, 9), (4, 16), (5, 25)]
sq_tup = [(i, i**2) for i in li]
print(sq_tup)


# Example - 9 - Sample i/p = [1, 2, 3, 4, 5]  Sample o/p = [(1,1), (2, 8), (3, 27), (4, 64), (5, 125)]
cube_tup = [(i, i**3) for i in li]
print(cube_tup)
