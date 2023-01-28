'''Exercício Python 008: Escreva um programa 
que leia um valor em metros e o exiba 
convertido em centímetros e milímetros.'''

centimetros = milimetros = 0
metros = float(input('Digite um valor em metros: '))
print()
centimetros = metros * 100
milimetros = metros * 1000
print(
    f'O valor em {metros} metros convertido para centrimetros é {centimetros:.0f}.')
print(
    f'O valor em {metros} metros convertido para milimitros é {milimetros:.0f}.')
print()
