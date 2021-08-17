"""
EXERCÍCIO 082: Dividindo Valores em Várias Listas

Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, cria duas listas extras que vão conter 
apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""

geral = []
pares = []
impares = []

print(30*'=')
print('Gerando listas de PARES e IMPARES')
print(30*'=')

while True:
    numero = int(input('Digite um valor: '))
    
    # Adicionando os números
    # Adicionando no geral
    geral.append(numero)
    #Verficando se é par ou impar para adicionar
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    # Condição de continuação
    print(30*'=')
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if op[0] in 'N':
        break

print(f'\nOs números digitados foram: \n{geral}')
print(f'Os pares são: \n{pares}')
print(f'Os ímpares são: \n{impares}')
    