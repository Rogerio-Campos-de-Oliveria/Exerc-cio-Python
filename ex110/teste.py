'''Exercício Python 109: Modifique as funções que form 
criadas no desafio 107 para que elas aceitem um parâmetro a 
mais, informando se o valor retornado por elas vai ser ou não 
formatado pela função moeda(), desenvolvida no desafio 108.'''

from ex110 import moeda



#import moeda - outra maneira

p = float(input('Digite o preço: R$ '))
print((f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}'))
print((f'O dobro de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.dogro(p))}'))
print((f'Aumentando 10%, temos R$ {moeda.moeda(moeda.aumentar(p, 10))}'))
print((f'Diminuindo 15%, temos R$ {moeda.moeda(moeda.diminuir(p, 15))}'))