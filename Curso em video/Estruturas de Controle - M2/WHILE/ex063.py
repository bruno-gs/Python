"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0

Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('Sequência de Fibonacci')

numero = int(input('Quntos termos você deseja? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM') 