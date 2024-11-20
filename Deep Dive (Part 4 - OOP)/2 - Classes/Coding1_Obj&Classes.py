class Person:
    pass

print(type(Person))             # <class 'type'>

print(type(type))               # <class 'type'>

print(Person.__name__)          # 'Person' -- data attribute name

p = Person()
print(type(p))                  # <class '__main__.Person'>

print(p.__class__)              # <class '__main__.Person'>

print(type(p) is p.__class__)   # True

print(isinstance(p, Person))    # True

print(isinstance(p, str))       # False

print(isinstance('Hello', str)) # True
