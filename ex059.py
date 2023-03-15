'''Exercício Python 059: Crie um programa que leia dois valores e 
mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
opção = tot = 0
num_01 = float(input('Digite o primeiro valor: '))
num_02 = float(input('Digite o primeiro valor: '))

while opção != 5:
      
      print('''
     
      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa 
      
      ''')    
      opção = int(input('Qual opção você deseja? '))
      print('=-=' * 10)
      if opção == 1:
            tot = num_01 + num_02
            print(f'A soma dos valores {num_01:.2f} e {num_02:.2f} é de {tot:.2f}')
      elif opção == 2:
            tot = num_01 * num_02
            print(f'A resultado de {num_01:.2f} x {num_02:.2f} é {tot:.2f}')
      elif opção == 3:
            if num_01 > num_02:
                  maior = num_01
            elif num_01 < num_02:
                  maior = num_02
            print(f'Entre {num_01:.2f} e {num_02:.2f} o maior valor é {maior:.2f}')
      elif opção == 4:
            print('informe os números novamente.')
            num_01 = float(input('Digite o primeiro valor: '))
            num_02 = float(input('Digite o primeiro valor: '))
      elif opção == 5:
            print('Finalizando......')
            sleep(1)
      else:
            print('Opção invalida! Tente novamente.')
      print('=-=' * 10)
            

print('Fim do programa !')