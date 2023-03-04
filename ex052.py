'''Exercício Python 52: Faça um programa que leia 
um número inteiro e diga se ele é ou não um número 
primo.'''


#Escolher o número que deseja saber se é PRIMO ou NÃO
número = int(input('Digite um número: '))
tot = 0
#Calculo para saber por quantos números ele é divisivel  
for c in range(1, número + 1):
    if número	% c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\33[mO número {número} foi divisível {tot} vezes.')
#Para ser PRIMO o numero deve ser divisivel por 1 e por ele mesmo, isto é 2 vezes.
if tot == 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele \033[31mNÃO \033[mé um número PRIMO!')
    