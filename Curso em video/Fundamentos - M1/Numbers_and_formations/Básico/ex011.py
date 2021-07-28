"""
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = 2 # Área que a tinta consegue pintar por litro
litros = area / tinta

print(f'A parede informada tem {largura:.2f} m de largura e {altura:.2f} m de altura, ocupando uma área de {area:.2f} m2.')
print(f'Para pintar essa parede serão necessários {litros:.2f} litros de tinta.')
