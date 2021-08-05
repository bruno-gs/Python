"""
EXERCÍCIO 060: Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
num = int(input('Digite o número para saber fatorial: '))
tot = num
for seq in range(num, 0, -1):
    if seq == num:
        print(f'{seq}! = {seq} x ',end='')
    elif seq == 1:
        print(f'{seq} = {tot}')
        break
    else:
        print(f'{seq} x ',end='')
        tot *= seq
print('Obrigado pela preferência!!')