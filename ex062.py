'''Exercício Python 62: Melhore o DESAFIO 61, 
perguntando para o usuário se ele quer mostrar mais 
alguns termos. O programa encerrará quando ele disser 
que quer mostrar 0 termos.'''

titulo = '10 TERMOS DE UMA PA'
print('=' * 40)
print(titulo.center(40))
print('=' * 40)
print()
primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Difite a razão: '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' → ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('=' * 40)
print(f'Progressão finalizada com {total} termos mostrados.')
print('=' * 40)