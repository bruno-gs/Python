"""
EXERCÍCIO 065: Maior e Menor Valores

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

total = quant = 0
while True:
    num = int(input('Digite um número: '))
    total += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor: 
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram digitados {quant} números e a média entre eles foi {total / quant:.2f}')
print(f'O maior foi {maior} e o menor foi {menor}')