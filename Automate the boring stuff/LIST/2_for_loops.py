'''
Lista de 0 a 3
    list(range(4))

lista de 0 a 99 pulando de 2 em 2
    list(range(0,100,2))



supplies = ['pens', 'paper', 'computer']
for i in range(len(suplies)):
    print(f'Index {i} in supplies is: {supplies[i]}')

'''


'''
multiple assignment

cat=['fat', 'orange', 'loud']

size, color, disposition = cat

or

size, color, disposition = 'skinny','black','quiet'
'''

'''
swapping variables -- trocando os valores entre variaveis

a = 'AAAA'
b = 'BBBB'

a,b = b,a
'''

'''
augmented assignment operators

spam = 42
spam += 1
spam /= 2
'''

'''
RECAP
A for loop technically iterates over the values in a list.
The range() function returns a list-like value, which can be passed to the list() function if you need an actual list value.
Variables can swap their values using multiple assignment: a, b = b, a
Augmented assignment operators like += are used as shortcuts.
'''