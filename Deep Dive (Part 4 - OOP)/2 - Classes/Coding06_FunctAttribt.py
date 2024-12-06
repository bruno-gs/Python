class Person:
    def say_hello():
        print("Hello")

Person.say_hello
print(type(Person.say_hello))   # <class 'function'>
Person.say_hello()              # Hello

p = Person()

p.say_hello
print(type(p.say_hello))    # <class 'method'>

#p.say_hello()               # TypeError: Person.say_hello() takes 0 positional arguments but 1 was given

class Person:
    def set_name(instance_obj, new_name):
        instance_obj.name = new_name

p = Person()
p.set_name('John')
print(p.__dict__)   # {'name': 'John'}

Person.set_name(p, 'Alex')
print(p.__dict__)   # {'name': 'Alex'}


class Person:
    def set_name(self, new_name):
        self.name = new_name


class Person:
    def say_hello(self):
        print(f'{self} says hello')

