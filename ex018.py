'''Exercício Python 18: Faça um programa que leia um 
ângulo qualquer e mostre na tela o valor do seno, cosseno 
e tangente desse ângulo.'''

import math

angulo = float(input('Digite o ângulo que você deseja saber: '))

# O python não calcula o valor digitado em ângulos e sim como radianos, então precisamos converter o valor digiado para radiano primeiro para ele dar os valores corretos.
número = math.radians(angulo)


#Programa com o número em radiano.

print(f'O ângulo de {angulo} tem o SENO de {math.sin(número):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {math.cos(número):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {math.tan(número):.2f}')

