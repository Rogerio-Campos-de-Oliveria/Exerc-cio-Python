'''Exercício Python 081: Crie um programa que vai 
ler vários números e colocar em uma 
lista.
Depois disso, mostre:

A) quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = ' '
    cont += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort(reverse=True)
print('=-=' * 20)
print(f'Foram digitados {cont} valores.')
print(f'Segue a lista em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
        