"""
EXERCÍCIO 084: Lista Composta e Análise de Dados

Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista = []
princ = []
mai = men = 0
while True:
    # Lista -- adiciona nome e peso -- nome em lista[0], peso em lista[1]
    lista.append(str(input('Digite o nome da pessoa: ')))
    lista.append(float(input('O peso da pessoa: ')))

    # Aqui estamos adicionando o peso maior e menor ao valor digitado primeiro
    if len(princ) == 0:
        mai = men = lista[1]

    # Analise os próximos inputs, para achar o maior e menor valor
    else:
        if lista[1] > mai:
            mai = lista[1]
        if lista[1] < men:
            men = lista[1]
    
    # aqui fazemos uma cópia da lista de digitação para a lista principal
    princ.append(lista[:])

    # zeramos a lista de input
    lista.clear()
    
    #condição para continuar
    op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break

#Finalizando
print('-=' * 30)
print(f'Foram cadastradas {len(princ)} pessoas.')

# Pegando o nome da pessoa com o maior peso 
print(f'O maior peso foi {mai}kg. Peso de', end=' ')
for f in princ:
    if f[1] == mai:
        print(f'[{f[0]}]', end=' ')

# Pegando o nome da pessoa com o menor peso
print(f'\nO menor peso foi {men}kg. Peso de', end=' ')
for f in princ:
    if f[1] == men:
        print(f'[{f[0]}]', end=' ')
