def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res


def aumentar(preço, taxa):
    res = preço * (1 + (taxa/100))
    return res


def diminuir(preço, taxa):
    res = preço * (1 - (taxa/100))
    return res
