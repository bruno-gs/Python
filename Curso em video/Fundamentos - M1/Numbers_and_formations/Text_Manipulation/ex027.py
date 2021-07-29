"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
nome = str(input('Seu nome completo é: ')).strip()
lista = nome.split()
print(f'Primeiro: {lista[0]}')
print(f'Último: {lista[len(lista) - 1]}')
