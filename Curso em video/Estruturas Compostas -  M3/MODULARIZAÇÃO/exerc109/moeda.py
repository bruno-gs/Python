def dobro(preço=0, formato=False):
    """
    Dobro de algum valor
    :param preço: Preço de algum produto ou alguma coisa.
    :param formato: Para atribuir a moeda real nos resultados
    :return: O resultado do dobro, e sua devida formatação
    """
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    """
    Metade de um valor
    :param preço: Valor que deseja saber a metade
    :param formato: Para atribuir a moeda real nos resultados
    :return: O resultado da metade, e sua devida formatação
    """
    res = preço / 2
    return res if not formato else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    """
    Saber o valor com uma devida porcentagem a mais.
    :param preço: Valor que deseja saber algum incremento
    :param taxa: incremento desejado
    :param formato: Para atribuir a moeda real nos resultados
    :return: O resultado do incremento, e sua devida formatação
    """
    res = preço * (1 + (taxa/100))
    return res if not formato else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    Saber o valor com uma devida porcentagem a menos.
    :param preço: Valor que deseja saber algum decremento
    :param taxa: decremento desejado
    :param formato: Para atribuir a moeda real nos resultados
    :return: O resultado do decremento, e sua devida formatação
    """
    res = preço * (1 - (taxa/100))
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    Utilizada para colocar a formatação de moeda no número.
    :param preço: preço que deseja colocar a formatação
    :param moeda: tipo da moeda: Reais, dólares, euro
    :return: mensagem formatada com o preço e mundanças para vírgula, além do início com o símbolo da moeda desejada.
    """
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
