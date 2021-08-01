"""
EXERCÍCIO 042: Analisando Triângulos v2.0

Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

cond1 = reta1 < (reta2 + reta3) 
cond2 = reta2 < (reta1 + reta3)
cond3 = reta3 < (reta1 + reta2)

equi = reta1 == reta2 == reta3
isos = reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1

if cond1 and cond2 and cond3:
    print('As retas PODEM formar um triângulo, sendo ele: ')
    if equi:
        print('EQUILÁTERO!')
    elif isos:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')

else:
    print('As retas NÃO PODEM formar um triângulo')