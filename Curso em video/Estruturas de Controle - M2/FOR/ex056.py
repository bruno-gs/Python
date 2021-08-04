"""
EXERCÍCIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
media = 0
maior = 0
f_menor = 0
for i in range(1,5):
    print(f'REFERENTE A PESSOA {i}')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO ([M] ou [F]): '))
    media += idade

    if sexo == 'M':
        if i == 1:
            maior = idade
            idoso = nome

        else:
            if idade > maior:
                maior = idade
                idoso = nome

    else:
        if idade < 20:
            f_menor +=1    

print(f'A média das idades ficou em {media/4:.2f} anos')
print(f'O homem mais velho é o senhor {idoso} com {maior} anos de idade')
print(f'No grupo temos {f_menor} mulheres com menos de 20 anos')
