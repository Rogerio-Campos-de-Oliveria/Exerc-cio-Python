'''Exercício Python 51: Desenvolva um programa que 
leia o primeiro termo e a razão de uma PA. No 
final, mostre os 10 primeiros termos dessa 
progressão.'''
titulo = '10 TERMOS DE UMA PA'
print('=' * 40)
print(titulo.center(40))
print('=' * 40)
print()
primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Difite a razão: '))
decimo = primeiro_termo + (10 - 1) * razão
for c in range(primeiro_termo, decimo + razão, razão):
    print(c, end=' → ')
print('ACABOU!')
    