'''Exercício Python 110: Adicione o módulo moeda.py
criado nos desafios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações
geradas pelas funções que já temos no módulo
criado até aqui.'''

from ex110 import moeda_110

#import moeda - outra maneira


p = float(input('Digite o preço: R$ '))
moeda_110.resumo(p)
