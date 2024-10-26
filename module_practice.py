
#from my_module import Person
#import my_module

#greet("John")
#person = Person("John", 30)
#person.greet()

from shared_resources import some_global_variable
from my_module import greet


print(some_global_variable)
greet("Tommy")