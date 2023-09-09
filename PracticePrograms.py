# Program 1
# Sample i/o = 5
# Sample o/p = 0 1 4 9 16
def calc_square():
    num = int(input("Enter a num: "))
    for i in range(0, num):
        print(i*i, end=" ")


calc_square()
print()


# Program 2
# Sample i/o = 1990
# Sample o/p = False

def is_leap():
    year = int(input("Enter year: "))
    if year > 999 and year <= 9999:
        if year % 4 == 0:
            print(True)
        else:
            print(False)
    else:
        print("Invalid Year(Must be 4 digits)!")


is_leap()
print()

# Program 3
# Sample i/o = 3
# Sample o/p = 123


def series():
    num = int(input("Enter a num: "))
    for i in range(1, num+1):
        print(i, end="")


series()
