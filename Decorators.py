from time import *


# Example 1
def performance(func):
    def inner(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"Time taken for execution {t2 - t1} s")
    return inner


@performance
def loop():
    for i in range(100):
        i*2


loop()


# Example 2
def decor(fn):
    def inner(name):
        if name == "Tom":
            print(name, " is eating BURGER!")
        else:
            fn(name)
    return inner


@decor
def eat(name):
    print(name, " is eating PIZZA!")


eat("Tom")
eat("Jerry")
eat("Nobita")
eat("Dora")


# Example 3
def smart_div(fn):
    def inner(a, b):
        if b == 0:
            print("Division not Possible!")
        else:
            fn(a, b)
    return inner


@smart_div
def div(a, b):
    print(a/b)


div(23, 0)
