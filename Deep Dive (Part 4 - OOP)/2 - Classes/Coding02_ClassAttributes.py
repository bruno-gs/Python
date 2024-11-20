class Program:
    language = 'Python'
    version = '3.8'

print(Program.language)         # Python
print(Program.version)          # 3.8

Program.version = '3.7'
print(Program.version)          # 3.7

print(getattr(Program, 'language', None))   # Python

setattr(Program, 'version', '3.8')
print(getattr(Program, 'version', None))    # 3.8

# Attribute not defined
# print(getattr(Program, 'x'))      # AttributeError: type object 'Program' has no attribute 'x'

print(getattr(Program, 'x', None))  # None

Program.x = 100
print(getattr(Program, 'x', None))  # 100

setattr(Program, 'x', -100)
print(Program.__dict__) # {'__module__': '__main__', 'language': 'Python', 'version': '3.8', '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None, 'x': -100}

delattr(Program, 'x')
print(Program.__dict__) # {'__module__': '__main__', 'language': 'Python', 'version': '3.8', '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}

Program.y = 'Hello'
print(Program.__dict__) # {'__module__': '__main__', 'language': 'Python', 'version': '3.8', '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None, 'y': 'Hello'}

del Program.y
print(Program.__dict__) # {'__module__': '__main__', 'language': 'Python', 'version': '3.8', '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}

# Access only one attribute at a time
print(Program.__dict__['language']) # Python

# Generate a list of attribute of the class
print(Program.__dict__.items()) # dict_items([('__module__', '__main__'), ('language', 'Python'), ('version', '3.8'), ('__dict__', <attribute '__dict__' of 'Program' objects>), ('__weakref__', <attribute '__weakref__' of 'Program' objects>), ('__doc__', None)])

