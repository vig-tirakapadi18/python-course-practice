# FOR LOOP
# Example: 1
'''str = "Vighnesh"

for i in str:
    print(i, end=" ")'''

# Example 2:
# WAPP to print nums from 1-n
'''n = int(input("Enter a limit: "))

for i in range(1, n+1):
    print(i, end=" ")'''

# WAPP to print table
'''num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")'''


# WHILE LOOP
# Example 1
'''i = 1
while (i <= 10):
    print("Hello ", i)
    i = i + 1'''


# WAPP to print 1-10 seperating each num with _
'''i = 1
while (i <= 10):
    print(i, end="_")
    i = i + 1'''


# WAPP to print num from 1-10 and break the loop at num == 5
'''i = 1
while (i <= 10):
    print(i)
    i = i + 1
    if i == 5:
        break'''


# WAPP to print num from 0 to -10 and break the loop at num == -6
'''i = 0

while i >= -10:
    print(i)
    i = i - 1
    if i == -6:
        break'''  # WAPP to print num from 0 to -10 and break the loop at num == -6


# WAPP to print num from 1-10, skipping 5
i = 0
while i <= 9:
    i = i + 1
    if i == 5:
        continue
    print(i)
