# Without try-except
class Demo1:
    def calc(self):
        a = 10
        b = 0
        # c = a / b  # Abrupt Termination
        # print(c)  # ZeroDivisionError: division by zero


d1 = Demo1()
d1.calc()

# With try-except


class Demo2:
    def calc(self):
        try:
            a = 10
            b = 0
            c = a / b
            print(c)
        except:
            print("OOPS! Error.")


d2 = Demo2()
d2.calc()


# Exception Handling in multiple methods
# Without try-except
'''def alpha():
    a = 10
    b = 0
    c = a / b
    print(c)


def beta():
    print("Beta connection established!")
    alpha()
    print("Beta connection ended!")


def gamma():
    print("Gamma connection established!")
    beta()
    print("Gamma connection ended!")


gamma()'''


# With try-except
def alpha1():
    a = 10
    b = 0
    c = 10 / 0
    print(c)


def beta1():
    print("Beta connection established!")
    alpha1()
    print("Beta connection ended!")


def gamma1():
    print("Gamma connection established!")
    try:
        beta1()
    except:
        print("Exception Handled in gamma!")
    print("Gamma connection ended!")


gamma1()


# try-except-else-finally
'''def divide():
    try:
        num1 = int(input("Enter 1st num: "))
        num2 = int(input("Enter 2nd num: "))
        res = num1 / num2
        print(res)
    except:
        print("except block executed!")
    else:
        print("else block executed!")
    finally:
        print("finally block executed!")


divide()
# CASE - 1: For a = 10, b = 2: try-else-finally
# CASE - 2: For a = 10, b = 0: try-except-finally'''


# Multiple except blocks
'''def divide1():
    try:
        num1 = int(input("Enter 1st num: "))
        num2 = int(input("Enter 2nd num: "))
        c = num1 / num2
        print(c)
    except ZeroDivisionError:
        print("Can't divide by Zero!")
    except NameError:
        print("Name Error occured!")
    except ValueError:
        print("Can not divide by string!")
    except:
        print("Error occured!")


divide1()'''


# User Defined Exception Handler
# Example 1
class InvalidAge(Exception):
    pass


def age():
    age = int(input("Enter Age: "))
    if age > 18:
        print("You are eligible!")
    else:
        raise InvalidAge


age()


# Example 2
class InvalidPinError(Exception):
    pass


def password():
    pin = int(input("Enter a pin: "))
    if pin == 1818:
        print("Correct pin!")
    else:
        raise InvalidPinError


try:
    password()
except:
    print("TWO attempts left!")
    try:
        password()
    except:
        print("ONE attempt left!")
        try:
            password()
        except:
            print("OOPS!...Account Blocked!")
