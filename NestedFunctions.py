# Example 1
def avg_of_nums():
    def add(n1, n2):
        return n1 + n2
    n1 = int(input("Enter 1st num: "))
    n2 = int(input("Enter 2nd num: "))
    res = add(n1, n2)
    avg = res / 2
    print(avg)


avg_of_nums()
