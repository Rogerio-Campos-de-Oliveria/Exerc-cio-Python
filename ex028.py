'''Exercício Python 28: Escreva um programa que faça o 
computador “pensar” em um número inteiro entre 0 e 5 e peça 
para o usuário tentar descobrir qual foi o número escolhido 
pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.'''
from random import randint
from time import sleep
print('-=-'*10)
print('Estou Pensando !!!! Vou pensar em um número 0 e 5. tente Adivinhar ...')
print('-=-'*10)
número = randint(0, 5)  # Faz o computador "pensar"
# Jogador tenta adivinhar
jogador = int(input('Boa sorte!!! Qual número eu pensei? '))
print('PROCESSANDO ...')
sleep(1.5)

if jogador == número:
    print('PARABÉNS!!!! Você acertou !!!')
else:
    print(f'ERROU!!! Eu pensei no número {número}.')
print('FIM !!!')
