'''
EXERCÍCIO 004: Dissecando uma variável
Faça um programa que leia algogo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
'''
algo = input('Digite qualgoquer coisa: ')
print('O que foi escrito tem tipo: ', type(algo))
print('É um algofanumérico?', algo.isalnum())
print('É um número? ', algo.isnumeric())
print('É uma string?', algo.isalpha())
print('Está em caps?', algo.isupper())
print('Está sem caps?', algo.islower())
print('Está capitalgoizada?', algo.istitle())  # Primeira maiúscula