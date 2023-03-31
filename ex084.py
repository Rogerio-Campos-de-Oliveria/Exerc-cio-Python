'''Exercício Python 084: Faça um programa que leia nome 
e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dados = list()
cadastro = []
maior = menor = 0

while True:
    
    cadastro.append(str(input('Digite o nome: ')))
    cadastro.append(float(input(f'Digite o peso: ')))
    
    if len(dados) == 0:
        maior = menor = cadastro[1]
    else: 
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
            
    dados.append(cadastro[:])
    cadastro.clear()
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('=-=' * 30)
print(f'Foram cadastrados {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end=' ')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}' , end='')
print()