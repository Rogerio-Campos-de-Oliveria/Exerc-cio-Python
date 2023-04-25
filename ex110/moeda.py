def aumentar(preço=0, taxa=0, formato=False):
    """

    Args:
        preço: valor digitado pelo usuário
        taxa: é juros cobrado em cima do preço
        formato: para mostrar o valor em moeda

    Returns: vai mostrar o valor já formatado para o usuário

    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)



def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)



def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)



def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')