'''
import random
random.randint(1,10)
'''

'''
import random, sys,os,math
'''

'''
from random import *
'''

'''
import sys
sys.exit()
'''

# import sys
# print('Hello')
# sys.exit() #Finaliza o programa
# print('Goodbye00') 


# Ensinando sobre a instalação de módulos com pip

# import pyperclip
# pyperclip.copy('Hello World!')
# pyperclip.paste()

#################################################################

#Escrevendo nossas funções -- A mini program in a program
# Evitar a duplicação de código

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()


# Com parâmetro
def hello(name):
    print(f'Hello {name}!')

# O argumento dentro da chamada
hello('Alice')
hello('Bob')



#With return
def plusOne(number):
    return number+1

newnumber = plusOne(5)
print(newnumber)

print('Hello', end ='') #Usado para q não haja um "Enter" pós seu print
print('Hello', 'World', sep ='NADA') #Usado para colocar o que terá no espaço entre as letras
print('Hello', 'World', sep =',') #Usado para colocar o que terá no espaço entre as letras



############################################################################################################

#Global and local functions
spam = 42 #global variable

def eggs():
    spam = 42 #local variable -- só existe quando a função funciona

print('Some code here')











