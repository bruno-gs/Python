"""
EXERCÍCIO 049: Tabuada v2.0

Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
print('TABUADA DE QUALQUER NÚMERO')
numero = int(input('Diga o número que deseja saber a tabuada: '))
for var in range(0,11):
    print(f'{numero} X {var} = {numero * var}')
