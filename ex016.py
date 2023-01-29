'''Exercício Python 16: Crie um programa que leia um
número Real qualquer pelo teclado e mostre na tela a sua 
porção Inteira.'''

import math

número = float(input('Digite um valor qualquer: '))
print(
    f'O valor digitado foi {número} e sua porção interia é {math.trunc(número)}.')
