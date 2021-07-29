"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

cidade = str(input('What is your name? ')).strip().upper()
lista = cidade.split()
conf = 'SILVA' in lista
print(f'Seu nome tem "Silva"? {conf}')
