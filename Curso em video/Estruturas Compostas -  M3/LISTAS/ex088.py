"""
EXERCÍCIO 088: Palpites Para a Mega Sena

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from time import sleep
from random import randint
jogo = []
varios = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
quant = int(input('Quantos jogos você quer sortear? '))
print('-='*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
for i in range(0, quant):#laço pra quantidade de jogo
    cont = 0
    while True:#laço para a criação de um jogo
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            varios.append(jogo[:])
            jogo.clear()
            break
    print(f'Jogo {i + 1}: {varios[i]}')
    sleep(2)
