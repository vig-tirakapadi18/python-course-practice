class Demo1:
    a = 10
    b = 20

    def __init__(self):
        self.x = 100
        Demo1.tech = "Python"

    @staticmethod
    def display():
        Demo1.fee = 24999

    @classmethod
    def cls_method(cls):
        cls.name = "Vig"
        cls.age = 23


def main():
    # print(Demo1.tech)     #Error
    d = Demo1()
    print(d.b)  # 20
    print(Demo1.a)  # 10
    print(d.tech)  # Python
    print(Demo1.tech)  # Python
    # print(Demo1.fee)  # Error because static method is not invoked yet
    Demo1.display()
    print(Demo1.fee)  # 24999
    Demo1.cls_method()
    print(Demo1.name)  # Vig
    # print(cls.age)  # Accessing static variable using "cls" is not possible
    print(Demo1.age)  # 23


main()
