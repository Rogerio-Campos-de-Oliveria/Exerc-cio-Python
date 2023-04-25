'''Exercício Python 107: Crie um módulo chamado moeda.py
que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse
módulo e use algumas dessas funções.'''

from ex107 import moeda

#import moeda - outra maneira

p = float(input('Digite o preço: R$ '))
print((f'A metade de R$ {p} é {moeda.metade(p)}'))
print((f'O dobro de R$ {p} é {moeda.dogro(p)}'))
print((f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}'))
print((f'Diminuindo 15%, temos R$ {moeda.diminuir(p, 15)}'))