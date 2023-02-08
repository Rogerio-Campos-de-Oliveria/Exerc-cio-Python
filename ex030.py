'''Exercício Python 30: Crie um programa que leia um número 
inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

número = int(input('Digite um número: '))
if número % 2 == 0:
    print(f'O número que você digitou é Par')
else:
    print(f'O número que você digitou é Ímpar')
