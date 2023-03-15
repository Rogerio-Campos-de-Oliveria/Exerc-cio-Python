'''Exercício Python 61: Refaça o DESAFIO 51, lendo o 
primeiro termo e a razão de uma PA, mostrando os 10 
primeiros termos da progressão usando a estrutura while.'''

titulo = '10 TERMOS DE UMA PA'
print('=' * 40)
print(titulo.center(40))
print('=' * 40)
print()
primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Difite a razão: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(termo, end=' → ')
    termo += razão
    cont += 1
print('FIM !')