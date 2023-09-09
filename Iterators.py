# Example 1
li = [10, 20, 30, 40, 50, 60, 70]

itr = iter(li)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# Example 2
itr = iter(li)

while True:
    try:
        print(next(itr), end=" ")
    except:
        break


print()
# Example 3
string = "likjhygfdcvboujyhtgfdsxcvbkloiuy"

itr_string = iter(string)

while True:
    try:
        print(next(itr_string), end=" ")
    except:
        break


print()
# Example 4
tup = ("hello", "hey", 123, True, 6+7j, 123.23456)

itr_tuple = iter(tup)

while True:
    try:
        print(next(itr_tuple), end=" ")
    except:
        break


print()
# Example 5
li = [2, 4, 6, 8, 10, 12, 14, 16]

even_itr = iter(li)

while True:
    try:
        print(next(even_itr), end=" ")
    except:
        break


print()
# Example 6
li = [1, 3, 5, 7, 9, 11, 13, 15]

odd_itr = iter(li)

while True:
    try:
        print(next(odd_itr), end=" ")
    except:
        break


print()
# Example 7
string = "YouHavePowerOverYourMindNotTheOutsideEvents!"

quote_itr = iter(string)

while True:
    try:
        print(next(quote_itr), end=" ")
    except:
        break


print()
# Example 8
tup2 = (4, 2, 6, 7, 0, 9, 12, 45, 67)

itr_tup2 = iter(tup2)

while True:
    try:
        print(next(itr_tup2), end=" ")
    except:
        break
