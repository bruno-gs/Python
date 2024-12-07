# Creating Attributes at Run-time

class Person:
    pass

p1 = Person()
p2 = Person()
p1.name = 'Alex'

print(p1.__dict__)      # {'name': 'Alex'}
print(p2.__dict__)      # {}

p1.say_hello = lambda: 'Hello!'

print(p1.say_hello)     # <function <lambda> at 0x000002075783CFE0>
print(p1.__dict__)      # {'name': 'Alex', 'say_hello': <function <lambda> at 0x000002FAB547CFE0>}

from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person('Eric')
p2 = Person('John')

def say_hello(self):
    return f'{self.name} says hello!!'

print(say_hello(p1))    # Eric says hello!!
print(say_hello(p2))    # John says hello!!

p1_say_hello = MethodType(say_hello, p1)
print(p1_say_hello)     # <bound method say_hello of <__main__.Person object at 0x000001B51E78FD50>>

p1.say_hello = p1_say_hello
print(p1.__dict__)      # {'name': 'Eric', 'say_hello': <bound method say_hello of <__main__.Person object at 0x00000247D527FD50>>}
print(p1.say_hello())   # Eric says hello!!
print(getattr(p1, 'say_hello')())   # Eric says hello!!


class Person:
    def __init__(self, name):
        self.name = name
    
    def register_do_work(self, func):
        # self._do_work = MethodType(func, self)
        setattr(self, 'do_work', MethodType(func, self))
    
    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)
    
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do_work method.')
    
math_teacher = Person('Eric')
english_teacher = Person('John')

# math_teacher.do_work()  # AttributeError: You must first register a do_work method.

def work_math(self):
    return f'{self.name} will teach differentials today'

math_teacher.register_do_work(work_math)
print(math_teacher.__dict__)    # {'name': 'Eric', 'do_work': <bound method work_math of <__main__.Person object at 0x0000022CEC349F90>>}
print(math_teacher.do_work())   # Eric will teach differentials today

def work_english(self):
    return f'{self.name} will analyze Hamlet today'

english_teacher.register_do_work(work_english)
print(english_teacher.__dict__)     # {'name': 'John', 'do_work': <bound method work_english of <__main__.Person object at 0x000002724B95A1D0>>}
print(english_teacher.do_work())    # John will analyze Hamlet today



