'''Exercício Python 103: Faça um programa que tenha uma 
função chamada ficha(), que receba dois parâmetros 
opcionais: o nome de um jogador e quantos gols ele 
marcou. O programa deverá ser capaz de mostrar a ficha 
do jogador, mesmo que algum dado não tenha sido 
informado corretamente.'''

def ficha (jog='<desconhecido>', gol=0):
    print('=-=' * 20)
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    print('=-=' * 20)

    
#Programa Principal
jogador = str(input('Digite o nome do jogador: '))
gols = str(input(f'Quantos gols o jogador fez? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)
