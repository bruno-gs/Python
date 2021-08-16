"""
EXERCÍCIO 079: Valores Únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

print(25*'=')
print('VALORES ÚNICOS')
print(25*'=')

unicos = []

while True:
    num = float(input('Digite um valor: '))

    # Condição para verificar se já esta na lista ou é novo 
    if num in unicos:
        print(f'O valor {num} já consta na lista.\n')
    else:
        unicos.append(num)
        print(f'O valor {num} foi adicionado a lista.\n')
    
    #Condição para continuação
    continua = str(input('Deseja continuar? [S/N] ')).upper()
    if continua[0] in 'N':
        break
    else:
        pass

# Em ordem crescente
unicos.sort()

print(f'Os valores digitados foram: {unicos}')

