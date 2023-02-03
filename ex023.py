'''Exercício Python 23: Faça um programa que leia um 
número de 0 a 9999 e mostre na tela cada um dos dígitos 
separados.'''

número = int(input('Digite um número de 0 a 9999: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10

print(f'Analisando o número {número}.')
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')
