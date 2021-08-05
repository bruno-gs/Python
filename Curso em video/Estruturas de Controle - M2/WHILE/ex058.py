"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

print('Pensando em um número entre 0 e 10...')
computador = randint(0,10)
sleep(2)

palpite = int(input('Digite seu palpite: '))
tentativas = 1

while palpite != computador:
    if palpite > computador:
        palpite = int(input('Menos... Tente novamente: '))
    else:
        palpite = int(input('Mais... Tente novamente: '))
    tentativas +=1
    # palpite = int(input('Errou!! Tente novamente: ')) 

print(f'PARABÉNS, você acertou! O valor pensado foi {computador} e você acertou com {tentativas} tentativas!')
