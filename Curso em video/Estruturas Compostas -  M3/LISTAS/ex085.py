"""
EXERCÍCIO 085: Listas com Pares e Ímpares

Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
"""

numeros=[[],[]]

for i in range(7):
    valor = int(input('\nDigite um valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(numeros)
