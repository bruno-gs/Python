"""
EXERCÍCIO 043: Índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Digite seu peso atual (em kg): '))
altura = float(input('Digite sua altura atual (em metros): '))

imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.2f}')

if imc <= 18.5:
    print('Abaixo do peso.')
elif imc > 40:
    print('Obesidade Mórbida')
elif imc > 18.5 or imc <= 25:
    print('Peso ideal')
elif imc > 25 or imc <=30:
    print('Sobrepeso')
else:
    print('Obesidade')