'''Exercício Python 010: Crie um programa que
leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos dólares ela pode comprar.'''

dolar = 5.21
saldo = 0
real = float(input('Digite o valor em reais que você quer converter R$ '))
saldo = real / dolar
print(
    f'O valor em dolares que você terá U$D {saldo:.2f} referente o valor em reais de R$ {real:.2f}.')
