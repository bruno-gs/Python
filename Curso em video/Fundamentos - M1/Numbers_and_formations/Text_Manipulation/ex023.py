"""
EXERCÍCIO 023: Separando Dígitos de um Número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""
numero = int(input('Informe um número: '))
print(f'A análise do número {numero} é: ')

'''Ocorre a divisão por inteiro primeiro, 
depois é dividido por 10 e pegamos o resto'''

unidade = (numero // 1) % 10 
dezenas = (numero // 10) % 10 
centenas = (numero // 100) % 10 
milhares = (numero // 1000) % 10 

print(f'O número tem {unidade} unidades.')
print(f'O número tem {dezenas} dezenas.')
print(f'O número tem {centenas} centenas.')
print(f'O número tem {milhares} milhares.')
