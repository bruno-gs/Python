"""
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

cond1 = reta1 < (reta2 + reta3) 
cond2 = reta2 < (reta1 + reta3)
cond3 = reta3 < (reta1 + reta2)

if cond1 and cond2 and cond3:
    print('As retas PODEM formar um triângulo')
else:
    print('As retas NÃO PODEM formar um triângulo')