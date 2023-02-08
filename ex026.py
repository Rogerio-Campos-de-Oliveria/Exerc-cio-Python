'''Exercício Python 026: Faça um programa que leia uma frase
pelo teclado e mostre quantas vezes aparece a letra "A", em 
que posição ela aparece a primeira vez e em que posição ela 
aparece a última vez.'''

frase = str(input('Escreva uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1} na frase.')
print(f'O última letra A apareceu na posição {frase.rfind("A")+1} na frase.')
