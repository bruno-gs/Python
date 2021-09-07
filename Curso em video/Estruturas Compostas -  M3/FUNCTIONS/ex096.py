def área(comp, larg):
    a = comp * larg
    print(f'A área de um terreno {comp:.2f}x{larg:.2f} é de {a:.2f}m².')


print('    Controle de Terrenos')
print('-'*30)
c = float(input('Comprimento (m): '))
l = float(input('Largura (m): '))
área(c, l)
