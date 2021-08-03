"""
EXERCÍCIO 046: Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
print('CONTAGEM REGRESSIVA PARA 2022!!')
for regressiva in range(10,-1,-1):
    print(regressiva)
    sleep(1)
print('FELIZ ANO NOVO!!')