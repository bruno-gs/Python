"""
EXERCÍCIO 037: Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:

- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""

numero = int(input('Digite um número para conversão: '))
escolha = int(input('''AS OPÇÕES
1 PARA BINÁRIO
2 PARA OCTADECIMAL
3 PARA HEXADECIMAL
Digite sua escolha: '''))

if escolha == 1:
    print(bin(numero)[2:])
elif escolha == 2:
    print(oct(numero))
elif escolha == 3: 
    print(hex(numero))
else:
    print('Você digitou um número fora da lista apresentada')