#
#
#
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(f"Hello, my name is {self.name}!")

def greet(name):
    print(f"Hello, {name}!")

print(Person)