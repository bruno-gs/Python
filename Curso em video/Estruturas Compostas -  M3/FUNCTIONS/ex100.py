from random import randint
from time import sleep
numeros = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    sleep(1.5)
    for i in range(5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    s = 0
    print(f'Somando os valores pares de {lista}, temos ', end='')
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'{s}.')


sorteia(numeros)
somaPar(numeros)
