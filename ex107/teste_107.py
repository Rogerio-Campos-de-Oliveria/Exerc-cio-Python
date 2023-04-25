'''Exercício Python 107: Crie um módulo chamado moeda_110.py
que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe 
esse módulo e use algumas dessas funções.'''


from ex107 import moeda_107

#import moeda - outra maneira

p = float(input('Digite o preço: R$ '))
print((f'A metade de R$ {p} é {moeda_107.metade(p)}'))
print((f'O dobro de R$ {p} é {moeda_107.dobro(p)}'))
print((f'Aumentando 10%, temos R$ {moeda_107.aumentar(p, 10)}'))
print((f'Diminuindo 15%, temos R$ {moeda_107.diminuir(p, 15)}'))