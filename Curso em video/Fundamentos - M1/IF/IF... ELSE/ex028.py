"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
print('JOGO DA ADIVINHAÇÃO')
comp = randint(0,5)
palpite = int(input('Digite seu palpite: '))

resultado = comp == palpite

if resultado:
    print(f'Você acertou! O número foi {comp}')
else:
    print(f'Você errou! O número foi {comp}')