'''Exercício Python 082: Crie um programa que vai 
ler vários números e colocar em uma lista. Depois 
disso, crie duas listas extras que vão conter 
apenas os valores pares e os valores ímpares 
digitados, respectivamente. Ao final, mostre o 
conteúdo das três listas geradas.'''

valores = []
valores_par = []
valores_impar = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        valores_par.append(n)
    else:
        valores_impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-=' * 20)    
print(f'Os valores digitados são: {valores}')
print(f'Os valores PARES digitados são: {valores_par}')
print(f'Os valores ÍMPARES digitados são: {valores_impar}')
print('=-=' * 20)    