def fatorial(num, show=False):
    """
    Cálculo de fatorial
    :param num: Número que deseja saber o fatorial.
    :param show: Saber o processo de cálculo do fatorial
    :return: Resultado do fatorial. Se quiser, de todo processo.
    """
    print('-' * 30)
    result = 1
    for i in range(num):
        if show == True:
            if num == 1:
                print(f'{num} = ', end='')
            else:
                print(f'{num} x ', end='')
        result *= num
        num -= 1
    return result


print(fatorial(5, True))
