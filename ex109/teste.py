'''Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga
 mostrar os números como um valor monetário formatado.'''


from ex109 import moeda

#import moeda - outra maneira

p = float(input('Digite o preço: R$ '))
print((f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}'))
print((f'O dobro de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.dogro(p))}'))
print((f'Aumentando 10%, temos R$ {moeda.moeda(moeda.aumentar(p, 10))}'))
print((f'Diminuindo 15%, temos R$ {moeda.moeda(moeda.diminuir(p, 15))}'))