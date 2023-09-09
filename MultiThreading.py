# Single Threaded Program
'''class Java:
    def learnJava(self):
        for i in range(1, 6):
            print("Learning Java! ", i)


class Python:
    def learnPython(self):
        for i in range(1, 6):
            print("Learning Python! ", i)


def main():
    j = Java()
    p = Python()
    j.learnJava()
    p.learnPython()


main()'''


# Multi Threading Program
'''from threading import *
from time import *


class Java(Thread):
    def run(self):
        for i in range(1, 6):
            print("learn Java!", i)
            sleep(2)


class Python(Thread):
    def run(self):
        for i in range(1, 6):
            print("Learn Python!", i)
            sleep(2)


def main():
    print("Main Start!")
    j = Java()
    p = Python()
    j.start()
    p.start()
    print("Main End!")


main()'''


# Multi Threading with join()




from threading import *
from time import *
class Java(Thread):
    def run(self):
        for i in range(1, 6):
            print("Learning Java!", i)
            sleep(2)


class Python(Thread):
    def run(self):
        for i in range(1, 6):
            print("Learning Python!", i)
            sleep(2)


def main():
    print("Main Start!")
    j = Java()
    p = Python()
    j.start()
    p.start()
    j.join()
    p.join()
    print("Main End!")


main()
