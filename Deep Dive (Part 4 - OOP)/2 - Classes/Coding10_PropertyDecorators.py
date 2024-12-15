def my_decorator(fn):
    print('decorating function')
    def inner(*args, **kwargs):
        print('running decorated function')
        result = fn(*args, **kwargs)
        return result
    return inner

def undecorated_function(a, b):
    print('running original function')
    return a + b

print(undecorated_function(1,2))

decorated_func = my_decorator(undecorated_function)

print(decorated_func(1,2))

undecorated_function = my_decorator(undecorated_function)
print(undecorated_function) # <function my_decorator.<locals>.inner at 0x00000171658FE200>


@my_decorator
def my_func(a, b):
    print('running original function')
    return a + b

print(my_func)  # <function my_decorator.<locals>.inner at 0x0000019C2528E2A0>

####################################
# Using the properties decorators

class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        """ The Person's name """
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


p = Person('Alex')
# Call the setter
p.name = 'Eric'
# Call the getter
print(p.name)

help(Person.name)
