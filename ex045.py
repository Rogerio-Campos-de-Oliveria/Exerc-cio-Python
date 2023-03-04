'''Exercício Python 45: Crie um programa que faça o 
computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''
      Escolha uma Opção:
      [1] Pedra
      [2] Papel
      [3] Tesoura
      ''')
while True:
      print('-=' * 11)
      jogador = int(input('Digite sua opção: '))
      print('-=' * 11)
      print('JO')
      sleep(1)
      print('KEN')
      sleep(1)
      print('PO!!!')
      print('-=' * 11)
      computador = randint(1, 3)
      print(f'Jogador jogou {itens[jogador-1]}')
      print('          x')
      print(f'Computador jogou {itens[computador-1]}.')
      print('-=' * 11)
      sleep(1)
      if computador == 1: #Computador jogou PEDRA
            if jogador == 1:
                  print('EMPATE')
            elif jogador == 2:
                  print('JOGADOR VENCE')
            elif jogador == 3:
                  print('COMPUTADOR VENCE')
            else:
                  print('JOGADA INVÁLIDA!')
                  
      elif computador == 2: #Computador jogou PAPEL
            if jogador == 1:
                  print('COMPUTADOR  VENCE')
            elif jogador == 2:
                  print('EMPATE')
            elif jogador == 3:
                  print('JOGADOR VENCE')
            else:
                  print('JOGADA INVÁLIDA!')
                  
      elif computador == 3: #Computador jogou TESOURA
            if jogador == 1:
                  print('JOGADOR VENCE')
            elif jogador == 2:
                  print('COMPUTADOR VENCE')
            elif jogador == 3:
                  print('EMPATE')
            else:
                  print('JOGADA INVÁLIDA!')
      print('-=' * 11)
      resp = ' '
      while resp not in 'SN':           
            resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
      if resp == "N":
            break
print('Até a PRÓXIMA!')