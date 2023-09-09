# Object Reference
class Demo1:
    def __init__(self):
        self.name = "Vig"

    def display(self):
        print(self.name)


d1 = Demo1()
print(d1)   # <__main__.Demo1 object at 0x000001C2E7F6B940>


class Demo2:
    def __init__(self):
        self.name = "Vig"

    def display(self):
        print(self.name)

    def __str__(self):
        return "Name is "+self.name


d2 = Demo2()
print(d2)


# Operator Overloading
# Example - 1
class Demo3:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Name is "+self.name

    def __add__(self, other):
        return self.name + other.name


d3 = Demo3("Vighnesh")
print(d3)

d31 = Demo3("VT")
print(d31)
print(d3+d31)


class Demo4:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'My age is {self.age}'

    def __add__(self, other):
        return self.age + other.age


d4 = Demo4(23)
print(d4)

d41 = Demo4(24)
print(d4+d41)
