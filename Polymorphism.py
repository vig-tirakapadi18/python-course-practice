# Polymorphism without Code Flexibility and Code Compactness
num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))


class Calculator:
    def calc(self): pass


class Add(Calculator):
    def calc(self):
        print(f"{num1 + num2}")


class Sub(Calculator):
    def calc(self):
        print(f"{num1 - num2}")


class Mul(Calculator):
    def calc(self):
        print(f"{num1 * num2}")


class Div(Calculator):
    def calc(self):
        print(f"{num1 / num2}")


a = Add()
a.calc()
s = Sub()
s.calc()
m = Mul()
m.calc()
d = Div()
d.calc()


# Polymorphism with Code Flexibility and Code Compactness
class Player:
    def play(self):
        print("Play!")

    def sleep(self):
        print("Sleep!")


class CricketPlayer(Player):
    def play(self):
        print("Playing cricket!")

    def sleep(self):
        print("Cricketer is sleeping!")


class FootballPlayer(Player):
    def play(self):
        print("Playing football!")

    def sleep(self):
        print("Footballer is sleeping!")


def games(ref):
    ref.play()
    ref.sleep()


c = CricketPlayer()
f = FootballPlayer()
games(c)
games(f)


# Duck Typing
class Calc:
    def calc(self):
        print("Result!")


class Add1:
    def calc(self, a, b):
        print(a+b)


class Sub1:
    def calc(self, a, b):
        print(a-b)


class Mul1:
    def calc(self, a, b):
        print(a*b)


class Div1:
    pass


def permit(ref):
    num1 = int(input("Enter 1st num: "))
    num2 = int(input("Enter 2nd num: "))
    ref.calc(num1, num2)


# permit(Add1())
# permit(Sub1())
# permit(Mul1())
# permit(Div1())  # AttributeError: 'Div1' object has no attribute 'calc'

# Solution of Error


def permit1(ref, a, b):
    if type(ref).__name__ == "Div1":
        print("Not implemented yet!")
    else:
        ref.calc(a, b)


permit1(Div1(), 23, 5)
