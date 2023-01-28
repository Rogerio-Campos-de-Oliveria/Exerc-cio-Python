'''Exercício Python 009: Faça um programa que leia um
número Inteiro qualquer e mostre na tela a sua tabuada.'''

while True:
    número = int(input('Qual tabuada você quer ver? '))
    print('-' * 30)
    for c in range(0, 11):
        valor = número * c
        print(f'{c} x {número:2} = {valor}')
    print('-' * 30)
    res = input('Deseja continuar? [S/N]  ').upper()
    if res == "N":
        break
