# Public Access Modifiers
class Demo1:
    def __init__(self):
        self.x = 100

    def disp(self):
        print(self.x)  # Yes inside same class


class Demo2:
    def disp2(self):
        d1 = Demo1()
        print(d1.x)  # Yes inside different class


d1 = Demo1()
print(d1.x)  # Yes outside the class

d2 = Demo2()
d2.disp2()


# Protected Access Modifiers
class Demo3:
    def __init__(self):
        self._x = 222

    def disp1(self):
        print(self._x)  # Yes inside same class


class Demo4(Demo3):
    def disp2(self):
        print(self._x)  # Yes inside inherited class


class Demo5:
    # def disp3(self):
    #     print(self._x)  # Error - Not accessable inside different class
    pass


d3 = Demo3()
d3.disp1()
# print(d3._x)  #Should not be accessed outside same class or inherited class

d4 = Demo4()
d4.disp1()
d4.disp2()


# Private Access Modifiers
class Demo6:
    def __init__(self):
        self.__x = 333

    def disp1(self):
        print(self.__x)  # Yes only and only inside same class


class Demo7:
    def disp2(self):
        #     print(self.__x)   #Not accessable inside different class
        d6 = Demo6()
        print(d6.__x)  # Shouldn't access outside the same class


class Demo8(Demo6):
    def disp2(self):
        print(self.__x)  # Shouldn't access inside inherited class


# Data Mangling - Accessing private variable outside the class
class Demo9:
    def __init__(self):
        self.__y = 999

    def disp1(self):
        print(self.__y)


d9 = Demo9()
d9.disp1()


class Demo10:
    def disp2(self):
        d9 = Demo9()
        print(d9._Demo9__y)
        # Correct way accessing private variable inside different class


d10 = Demo10()
d10.disp2()


class Demo11(Demo9):
    def disp3(self):
        # print(self._Demo9__y)
        d9 = Demo9()
        # print(d9._Demo9__y)
