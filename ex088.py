'''Exercício Python 088: Faça um programa que ajude um 
jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo 
em uma lista composta.'''

from random import randint
from time import sleep

lista = list()
jogos = []

print('=-=' * 20)
print('JOGO DA MEGA SENA'.center(58))
print('=-=' * 20)

quant = int(input('Quantos palpites você deseeja? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-=' * 20)
print('=-=' * 3, f'SORTEANDO {quant} JOGOS ', '=-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)    

print('=-=' * 5 , '< BOA SORTE! >', '=-=' * 5)
