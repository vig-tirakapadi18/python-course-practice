# Object Creation in Python
# Example - 1
class Fan:
    def __init__(self):
        self.brand = 'USHA'
        self.price = 3500

    def rotate(self):
        print("Fan is Rotating!")


fan = Fan()
print(fan.brand)
print(fan.price)
fan.rotate()


# Example - 2
class Student:
    def __init__(self):
        self.name = 'Vighnesh'
        self.age = 22
        self.reg_no = 'KODNMO034'

    def study(self):
        print("Studying!")

    def read(self):
        print("Reading!")

    def listen(self):
        print('Listening!')


stud = Student()
print(stud.name)
print(stud.age)
print(stud.reg_no)
stud.study()
stud.read()
stud.listen()


# Example - 3
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def work(self):
        print("Working!")

    def read(self):
        print("Reading!")

    def sleep(self):
        print("Sleeping!")


emp1 = Employee('Vighnesh', 'E101', 35000)
print(emp1.name)
print(emp1.emp_id)
print(emp1.salary)
emp1.sleep()
emp1.work()
emp1.read()

emp2 = Employee("Vish", 'E102', 45000)
print(emp2.name)
print(emp2.emp_id)
print(emp2.salary)
emp2.sleep()
emp2.read()
emp2.work()


# main() in Python:
class Student2:
    def __init__(self):
        self.name = "Vighnesh"
        self.age = 22

    def study(self):
        print("Studying!")

    def read(self):
        print("Reading!")


def main():
    s = Student2()
    print(s.name)
    print(s.age)
    s.study()
    s.read()


main()


# Local, Static and Instance Variables
class Demo:
    a = 1000  # Static Variable

    def __init__(self):
        self.name = "Vighnesh"  # Instance Variable

    def greet(self):
        word = "Good Morning!"  # Local Variable
        print(word)
        print(self.name)
        print(Demo.a)


demo = Demo()
demo.greet()


# Method Overloading
'''class Demo2:
    def disp(self):
        print("0-Parameterized Method!")

    def disp(self, a):
        print("1-Parameterized Method!")

    def disp(self, a, b):
        print("2-Parameterized Method!")


demo2 = Demo2()
demo2.disp()
demo2.disp(10)
demo2.disp(10, 20)'''


# Constructor Overloading - Doesn't support
'''class Demo3:
    def __init__(self):
        print("0-Parameterized Constructor!")

    def __init__(self, a):
        print("1-Parameterized Constructor!")

    def __init__(self, a, b):
        print("2-Parameterized Constructor!")


demo3 = Demo3()'''



