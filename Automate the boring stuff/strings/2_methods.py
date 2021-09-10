'''
coloca todas as letras em maiusculo
spam = spam.upper()

coloca todas as letras em minusculo
spam = spam.lower()

para comparar ou qq coisa do tipo,
    são precisos cuidados com as letras

'''

'''
so funciona com Letras
spam = isupper() -- True or False

spam.islower() -- True or False
'''

'''
isalpha()   -- só letras

isalnum()   -- so letras e numeros

isdecimal() -- só numeros

isspace()   -- espaço em branco

istitle()   -- só titulo
'''






'''
RECAP
upper() and lower() return an uppercase or 
    lowercase string.

isupper(), islower(), isalpha(), isalnum(), 
    isdecimal(), isspace(), istitle() 
            returns True or False if the string 
            is that uppercase, lowercase, 
            alphabetical letters, and so on.

startswith() and endswith() also return bools.
    -- mostra se aquele é o inicio ou o fim

‘,'.join([‘cat', ‘dog']) returns a string 
    that combines the strings in the given list.
    -- cat , dog
    -- coloca entre aspas simples oq deseja ser a 
        separação

‘Hello world'.split() returns a list of strings 
    split from the string it's called on.


rjust() ,ljust(), center() 
    returns a string padded with spaces.
    -- coloca a string para um lado ou outro
        baseado no valor que precise

strip(), rstrip(), lstrip() returns a string 
    with whitespace stripped off the sides.
    -- tira os espaços de tudo / direita e esquerda

replace() will replace all occurrences 
    of the first string argument with the second 
        string argument.

Pyperclip has copy() and paste() 
    functions for getting and putting strings 
        on the clipboard.
'''