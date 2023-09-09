from abc import ABC, abstractmethod
# Abstraction Example:


class Player(ABC):
    @abstractmethod
    def play(self):
        pass


class Cricket(Player):
    def play(self):
        print("Playing Cricket!")


class Football(Player):
    def play(self):
        print("Playing Football")


c = Cricket()
c.play()
f = Football()
f.play()


# Rules of Abstraction
# Rule - 1 --- We can create empty abstract class
class Player1(ABC):
    pass


p = Player1()


# Rule - 2 --- We can create object if the abstract class contains only
#               concrete method then we can also invoke that method
class Player2(ABC):
    def play(self):
        print("Playing!")


p2 = Player2()
p2.play()


# Rule - 3 --- We can not create object if the class contains Abstract method(atleast 1)
#               we can create object if the class contains ALL Concrete Methods(ALL must be Concrete)
class Player3(ABC):
    def play(self):
        print("Playing!")

    @abstractmethod
    def sleep(self):
        print("Sleeping!")


# p3 = Player3()    #Can not create object
# p3.play()
# p3.sleep()


# Rule - 4 --- We can not create object of the Child Class
#              if we dont provide body for all the abstract methods of Parent Class
class Player4(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class CrickerPlayer(Player4):
    def play(self):
        print("Playing!")

    # Not providing body for sleep abstract method


# cp = CrickerPlayer()  #Can not create object
# cp.play()
# cp.sleep()


# Rule - 5 --- We can create object if the child class
#               has provided body for all the parent class abstract methods
class Player5(ABC):
    @abstractmethod
    def play(self): pass

    @abstractmethod
    def sleep(self): pass


class FootballPlayer(Player5):
    def play(self):
        print("Playing!")

    def sleep(self):
        print("Sleeping!")


fp = FootballPlayer()
fp.play()
fp.sleep()
