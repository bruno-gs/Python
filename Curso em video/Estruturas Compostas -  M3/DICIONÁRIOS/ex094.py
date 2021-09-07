"""
EXERCÍCIO 094: Unindo Dicionários e Listas

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""

pessoas_cadatradas = []
pessoa_atual = {}

somatoria_idades = media_idades= 0

while True:
    pessoa_atual.clear()
    pessoa_atual['Nome']    = str(input('Nome: ')).upper()
    pessoa_atual['Sexo']    = str(input('Sexo: ')).upper()
    pessoa_atual['Idade']   = int(input('Idade: '))
    
    somatoria_idades += pessoa_atual['Idade']

    pessoas_cadatradas.append(pessoa_atual.copy())

    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if resp[0] == 'N':
        break

print(f'\nFinalizado o preenchimento das pessoas\n')

print(f'Tivemos ao todo, {len(pessoas_cadatradas)} pessoas cadastradas.')

media_idades = (somatoria_idades/len(pessoas_cadatradas))

print(f'A média de idade das pessoas ficou em: \n{media_idades:.2f} anos')

print(f'As mulheres cadastradas são:\n')

for sex in pessoas_cadatradas:
    if sex['Sexo'] in 'Ff':
        print(f'{sex["Nome"]}')

print(f'Para finalizar, as pessoas acima da idade média são: ')

for idade in pessoas_cadatradas:
    if idade['Idade'] > media_idades:
        print(f'{idade["Nome"]}')

print(f'<<< FINALIZADO >>>')