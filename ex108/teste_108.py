'''Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga
 mostrar os números como um valor monetário formatado.'''


from ex108 import moeda_108

#import moeda - outra maneira

p = float(input('Digite o preço: R$ '))
print((f'A metade de R$ {moeda_108.moeda(p)} é {moeda_108.moeda(moeda_108.metade(p))}'))
print((f'O dobro de R$ {moeda_108.moeda(p)} é {moeda_108.moeda(moeda_108.dobro(p))}'))
print((f'Aumentando 10%, temos R$ {moeda_108.moeda(moeda_108.aumentar(p, 10))}'))
print((f'Diminuindo 15%, temos R$ {moeda_108.moeda(moeda_108.diminuir(p, 15))}'))