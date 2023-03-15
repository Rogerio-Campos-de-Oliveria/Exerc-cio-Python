'''Exercício Python 060: Faça um programa que leia um 
número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

print('=-=' * 20)
núm = int(input('Digite um numero para calcular o seu Fatorial: '))
c = núm
f = 1
print('=-=' * 20)
print(f'Calculando {núm}!')
while c > 0:
    print(f'{c} ', end='')
    print( 'x ' if c > 1 else '= ', end = '')
    f = f * c
    c -= 1

print(f'{f}')
print('=-=' * 20)