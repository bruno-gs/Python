class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}!')


p = Program()
print(type(p))                  # <class '__main__.Program'>
print(isinstance(p, Program))   # True

print(p.__dict__)       # {}
print(Program.__dict__) # {'__module__': '__main__', 'language': 'Python', 'say_hello': <function Program.say_hello at 0x000001E3F52DD260>, '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}

print( p.__class__)     # <class '__main__.Program'>



