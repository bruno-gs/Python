"""
EXERCÍCIO 069: Análise de Dados do Grupo

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
print('Bem-vindo(a). Faremos uma Análise de Dados do Grupo')
inicio = 1
homens = mulheres = maiores = 0
while True:
    idade = int(input(f'Digite o nome da pessoa {inicio}:'))
    sexo = str(input(f'Digite o sexo dessa pessoa [F/M]:')).strip().upper()[0]

    # HOMENS
    if sexo == 'M':
        homens +=1
    
    # Mulheres com menos de 20
    else:
        if idade < 20:
            mulheres += 1

    # Pessoas maiores de 18 anos
    if idade > 18:
        maiores += 1

    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos')
print(f'Foram cadastradas {homens} pessoas do sexo masculino')
print(f'Tivemos {mulheres} mulheres com menos de 20 anos')