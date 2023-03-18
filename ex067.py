'''Exercício Python 67: Faça um programa que mostre a 
tabuada de vários números, um de cada vez, para cada 
valor digitado pelo usuário. O programa será 
interrompido quando o número solicitado for negativo.'''


while True: 
    print('=-=' * 20)
    n = int(input('Que ver a tabuada de qual valor: '))
    print('=-=' * 20)
    if n < 0:
        break
    for c in range(0, 11):
        print (f'{n} x {c} = {n*c}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
print('=-=' * 20)