'''Exercício Python 102: Crie um programa que tenha uma 
função fatorial() que receba dois parâmetros: o 
primeiro que indique o número a calcular e outro 
chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de 
cálculo do fatorial.'''

def fatorial(num, show=False):
    print('=-=' * 20)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            if c == 1:
                print(' = ', end='')
        f *= c
    
    return f
    
#Principal Programa

n = int(input('Digite o número que deseja ver o fatorial: '))
situação = ' '
resp = str(input('Deseja mostrar o cálculo? [S/N] ')).upper()[0].strip()
if resp == 'S':
    situação = True
else:
    situação = False
print(fatorial(n,show=situação))