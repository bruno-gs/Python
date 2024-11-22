class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}!')


print(Program.__dict__)     # {'__module__': '__main__', 'language': 'Python', 'say_hello': <function Program.say_hello at 0x000002BBAB83D260>, '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}

print(Program.say_hello, getattr(Program, 'say_hello'))
# <function Program.say_hello at 0x000001543A5CD260> <function Program.say_hello at 0x000001543A5CD260>

Program.say_hello() # Hello from Python!

getattr(Program, 'say_hello')()     # Hello from Python!

Program.__dict__['say_hello']()     # Hello from Python!
