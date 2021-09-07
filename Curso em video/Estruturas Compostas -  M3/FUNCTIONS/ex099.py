def maior(* num):
    cont = mai = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont+=1
    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valor é {mai}.')


maior(9, 8, 4, 3, 2)
maior(4, 7, 0)