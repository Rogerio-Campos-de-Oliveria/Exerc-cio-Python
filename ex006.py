'''Exercício Python 006: Crie um algoritmo que leia um
número e mostre o seu dobro, triplo e raiz quadrada.'''
dobro = triplo = raiz_quadrada = 0
número = int(input('Digite um número: '))
dobro = número * 2
triplo = número * 3
raiz_quadrada = número ** (1/2)
print(f'O dobro do número {número} é {dobro}.')
print(f'O triplo do número {número} é {triplo}.')
print(f'A raíz quadrada do número {número} é {raiz_quadrada:.2f}.')
