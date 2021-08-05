"""
EXERCÍCIO 057: Validação de Dados

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
print('Nos conte seu sexo. Programa só aceita Masculino e Feminino.')
print('''[M] PARA MASCULINO
[F] PARA FEMININO''')
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Digite uma das opções válidas para sexo [M] ou [F]: ')).strip().upper()[0]

print(f'O sexo informado foi {sexo}')
