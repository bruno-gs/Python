class Person:
    def __init__(self):
        print(f'Initializing a new Person object: {self}')


p = Person()        # Initializing a new Person object: <__main__.Person object at 0x000001C77FB5F210>

class Person:
    def __init__(self, name):
        self.name = name

p = Person('Josh')
print(p.__dict__)   # {'name': 'Josh'}

