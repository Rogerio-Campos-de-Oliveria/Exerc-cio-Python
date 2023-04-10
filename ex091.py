'''Exercício Python 091: Crie um programa onde 4 
jogadores joguem um dado e tenham resultados 
aleatórios. Guarde esses resultados em um dicionário em 
Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador_01': randint(1, 6),
        'jogador_02': randint(1, 6),
        'jogador_03': randint(1, 6),
        'jogador_04': randint(1, 6)        
        }
ranking = list()
print('Valors sorteados:')
for k, v in jogo.items():
    print(f'{k} itrou {v} no dado.')
    sleep(1)
    
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # PARTE MAIS IMPORTANTE DO CÓDIGO

print('=-=' * 20)
print('== RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)