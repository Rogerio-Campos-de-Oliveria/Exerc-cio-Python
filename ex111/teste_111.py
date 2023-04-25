
'''Exercício Python 110: Adicione o módulo moeda.py
criado nos desafios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações
geradas pelas funções que já temos no módulo
criado até aqui.'''

from ex111 import moeda_111



#import moeda_111 # outra maneira


p = float(input('Digite o preço: R$ '))
moeda_111.resumo(p)
