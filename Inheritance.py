# Single Inheritance
class Demo1:
    def disp1(self):
        print("Demo1 disp1")


class Demo2(Demo1):
    def disp2(self):
        print("Demo2 disp2")


d2 = Demo2()
d2.disp1()
d2.disp2()


# Hirarchical Inheritance
class Demo3:
    def disp1(self):
        print("Demo3 disp1")


class Demo4(Demo3):
    def disp2(self):
        print("Demo4 disp2")


class Demo5(Demo3):
    def disp3(self):
        print("Demo5 disp3")


d4 = Demo4()
d4.disp1()
d4.disp2()

d5 = Demo5()
d5.disp1()
d5.disp3()


# Multi-level Inheritance
class Demo6:
    def disp1(self):
        print("Demo6 disp1")


class Demo7(Demo6):
    def disp2(self):
        print("Demo7 disp2")


class Demo8(Demo7):
    def disp3(self):
        print("Demo8 disp3")


d8 = Demo8()
d8.disp1()
d8.disp2()
d8.disp3()


# Multiple Inheritance
class Demo9:
    def disp1(self):
        print("Demo9 disp1")


class Demo10:
    def disp2(self):
        print("Demo10 disp2")


class Demo11(Demo9, Demo10):
    def disp3(self):
        print("Demo11 disp3")


d11 = Demo11()
d11.disp1()
d11.disp2()
d11.disp3()

print(Demo11.mro())

# MRO with Constructors
# CASE - 1


class Demo12:
    def __init__(self):
        self.x = 111


class Demo13:
    def __init__(self):
        self.y = 222


class Demo14(Demo12, Demo13):
    pass


d14 = Demo14()
# print(d14.y)  # Error - AttributeError: 'Demo14' object has no attribute 'y'


# CASE - 2
class Demo15:
    pass


class Demo16:
    def __init__(self):
        self.x = 100


class Demo17(Demo15, Demo16):
    pass


d17 = Demo17()
print(d17.x)  # 100


# Are Constructors inherited or not?
# Example - 1
class Demo18:
    def __init__(self):
        print("Demo18 Parent")


class Demo19(Demo18):
    def __init__(self):
        # If child has constructor then it will call Child constructor
        print("Demo19 Child")


d19 = Demo19()  # Demo19 Child


# Example - 2
class Demo20:
    def __init__(self):
        print("Demo20 Parent")


class Demo21(Demo20):
    pass


d21 = Demo21()  # Demo20 Parent


# Example - 3
class Demo22:
    def __init__(self):
        print("Demo22 Parent")


class Demo23(Demo22):
    def __init__(self):
        print("Demo23 Child")  # Demo23 Child
        super().__init__()  # Demo22 Parent


d23 = Demo23()


# Method Chaining
class GrateGrandFather:
    def cook(self):
        print("GrateGrandfather is cooking!")


class GrandFather(GrateGrandFather):
    def cook(self):
        print("GrandFather is cooking!")


class Father(GrandFather):
    def cook(self):
        print("Father is cooking!")


class Child(Father):
    def cook(self):
        print("Child is cooking!")  # Child is cooking!
        super().cook()  # Father is cooking!
        super(Father, self).cook()  # GrandFather is cooking!
        super(GrandFather, self).cook()  # GrateGrandfather is cooking!


c = Child()
c.cook()


# Types of Methods
class Papa:
    def kind(self):
        print("Bekind to everyone!")

    def cook(self):
        print("Parent cooking!")


class Beta(Papa):
    def cook(self):
        print("Beta is cooking!")

    def play(self):
        print("Playing!")


b = Beta()
b.kind()  # Bekind to everyone!
b.cook()  # Beta is cooking!
b.play()  # Playing!
