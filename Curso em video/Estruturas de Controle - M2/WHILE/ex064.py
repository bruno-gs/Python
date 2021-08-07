"""
EXERCÍCIO 064: Tratando Vários Valores v1.0
 
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""
soma = quant = 0

print('SOMA E QUANTIDADE DE NÚMERO COLOCADOS')
while True:
    numeros = int(input('Digite um número [999 para sair]: '))
    if numeros == 999:
        break
    soma+=numeros
    quant+=1

print(f'Foram digitados {quant} números e a soma resultou em {soma}.')