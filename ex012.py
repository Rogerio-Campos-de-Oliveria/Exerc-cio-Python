'''Exercício Python 12: Faça um algoritmo que leia 
o preço de um produto e mostre seu novo preço, 
com 5% de desconto.'''

produto = float(input('Digite o valor do produto: R$ '))
valor = produto - produto * 5 / 100
print(f'O valor a ser pago com o desconto de 5% é de R$ {valor:.2f}')
