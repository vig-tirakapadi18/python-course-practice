# import Module1    #Importing whole module

# Module1.add(20, 30)
# Module1.sub(30, 2)


# import Module1 as mod1    #Giving alias to imported module

# mod1.add(10, 20)
# mod1.sub(10, 20)


# from Module1 import add, sub  # Importing specific functions

# add(11234, 123)
# sub(1432, 1234)


from Module1 import add, sub

if __name__ == "__main__":
    add(1000, 100)
elif __name__ == "Module2":
    sub(2000, 786)
