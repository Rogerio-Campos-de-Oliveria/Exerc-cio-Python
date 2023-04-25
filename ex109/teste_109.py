'''Exercício Python 109: Modifique as funções que foram
criadas no desafio 107 para que elas aceitem um parâmetro a 
mais, informando se o valor retornado por elas vai ser ou não 
formatado pela função moeda(), desenvolvida no desafio 108.'''



from ex109 import moeda_109


#import moeda - outra maneira

p = float(input('Digite o preço: R$ '))
print((f'A metade de R$ {moeda_109.moeda(p)} é {moeda_109.metade(p, True)}'))
print((f'O dobro de R$ {moeda_109.moeda(p)} é {moeda_109.dobro(p, True)}'))
print((f'Aumentando 10%, temos R$ {moeda_109.aumentar(p, 10, True) }'))
print((f'Diminuindo 15%, temos R$ {moeda_109.diminuir(p, 15, True)}'))

