# Properties Lesson: Get and Set functions to protect attributes

class Person:
    def __init__(self, name):
        self.name = name

p = Person('Alex')
print(p.__dict__)   # {'name': 'Alex'}

p.name = 'No one'
print(p.__dict__)   # {'name': 'No one'}

class Person:
    def __init__(self, name):
        #self._name = name   # underscore name is a private attribute | convention
        self.set_name(name)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('Name must be a non-empty string')

p = Person('Alex')
try:
    p.set_name(100)
except ValueError as ex:
    print(ex)               # Name must be a non-empty string

print(p.__dict__)           # {'_name': 'Alex'}

print(p.get_name())         # Alex

p.set_name('Erick')
print(p.get_name())         # Erick



class Person:
    def __init__(self, name):
        self._name = name   # underscore name is a private attribute | convention

    def get_name(self):
        print('getter called...')
        return self._name
    
    def set_name(self, value):
        print('setter called...')
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('Name must be a non-empty string')
    
    name = property(fget=get_name, fset=set_name)

p = Person('Alex')
print(p.name)           # getter called... Alex

p.name = 'Eric'         # setter called...
print(p.__dict__)       # {'_name': 'Eric'}

print(getattr(p, 'name'))   # getter called... Eric

print(setattr(p, 'name', 'Alex')) # setter called...
print(getattr(p, 'name'))       # getter called... Alex
print(p.__dict__)       # {'_name': 'Alex'}



class Person:
    def __init__(self, name):
        self._name = name   # underscore name is a private attribute | convention

    def get_name(self):
        print('getter called...')
        return self._name
    
    def set_name(self, value):
        print('setter called...')
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('Name must be a non-empty string')
    
    def del_name(self):
        print('Deleter called...')
        del self._name
    
    name = property(fget=get_name, fset=set_name, fdel=del_name)

p = Person('Mark')
print(p.__dict__)   # {'_name': 'Mark}

del p.name          # Deleter called...
print(p.__dict__)   # {}

#print(p.name)       # AttributeError: 'Person' object has no attribute '_name'. Did you mean: 'name'?
# We deleted the information, so the instance has no value. You can create again the information.



# Doc String to know the purpose of the class
class Person:
    """This is a Person object"""
    def __init__(self, name):
        self._name = name   # underscore name is a private attribute | convention

    def get_name(self):
        print('getter called...')
        return self._name
    
    def set_name(self, value):
        print('setter called...')
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('Name must be a non-empty string')
    
    def del_name(self):
        print('Deleter called...')
        del self._name
    
    name = property(fget=get_name, fset=set_name, fdel=del_name, doc="The person's name")


help(Person)        # all information about the class

help(Person.name)   # Help on property: The person's name