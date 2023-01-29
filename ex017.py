'''Exercício Python 17: Faça um programa que leia o 
comprimento do cateto oposto e do cateto adjacente de um 
triângulo retângulo. Calcule e mostre o comprimento da 
hipotenusa.'''

from math import hypot

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)

print(f'A hipotenusa dos catetos {cateto_oposto} x {cateto_adjacente} é {hipotenusa:.2f}')
