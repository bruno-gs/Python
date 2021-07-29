
"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
junto = ''.join(lista)

print(f'Em MAIÚSCULAS: {nome.upper()}.')
print(f'Em minúsculas: {nome.lower()}.')
print(f'Seu primeiro nome tem {len(lista[0])} letras.')
print(f'Seu nome possui {len(junto)} letras.')
