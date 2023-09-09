# WAPP to add 2 nums using function
# Type - 1 Function
'''def add():
    n1 = int(input("Enter 1st Num: "))
    n2 = int(input("Enter 2nd Num: "))
    print(f"The addition of {n1} and {n2} : {n1+n2}")


add()'''


# Type - 2 Function
'''def add(n1, n2):
    print(f"Addition is: {n1+n2}")


n1 = int(input("Enter 1st num: "))
n2 = int(input("Enter 2nd num: "))
add(n1, n2)'''


# Type - 3 Function
'''def add():
    n1 = int(input("Enter 1st num: "))
    n2 = int(input("Enter 2nd num: "))
    return n1 + n2


sum = add()
print(f"The Addition is {sum}")'''


# Type - 4 Function
def add(n1, n2):
    return n1 + n2


n1 = int(input("Enter 1st num: "))
n2 = int(input("Enter 2nd Num: "))
sum = add(n1, n2)
print(f"The sum of {n1} and {n2} is {sum}")
