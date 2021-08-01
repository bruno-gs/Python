"""
EXERCÍCIO 045: Pedra, Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""
from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('=-='*10)
print('JOKENPÔ VIRTUAL')
print('=-='*10)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('JO')
sleep(1)
print('KEN')
sleep(1)
jog = int(input('Digite sua jogada? '))
print('PÔ')
sleep(1)
print('ANALISANDO...')
sleep(2)
print('-='*10)
print('Computador jogou {}'.format(itens[comp]))
print('O jogador jogou {}'.format(itens[jog]))
print('-='*10)

if comp == 0: #PEDRA
    if jog == 0:
        print('JOGADOR VENCE!')
    elif jog == 1:
        print('JOGADOR VENCE!')
    elif jog == 2:
        print('PC VENCE')
    else:
        print('JOGADA INVÁLIDA')
    
elif comp == 1: #PAPEL
    if jog == 0:
        print('PC VENCE')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')

elif comp == 2: #TESOURA
    if jog == 0:
        print('JOGADOR VENCE!')
    elif jog == 1:
        print('PC VENCE')
    elif jog == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')

else:
    print('SE TÁ LOCÃO E DIGITOU ALGO ERRADO')