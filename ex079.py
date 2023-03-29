'''Exercício Python 079: Crie um programa onde o 
usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista 
lá dentro, ele não será adicionado. No final, serão 
exibidos todos os valores únicos digitados, em 
ordem crescente.'''

valores = list()
while True:
    número = int(input('Digite um número: '))
    if número not in valores:
        valores.append(número)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja incluir outro número? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort()
print('=-=' * 20)
print(f'Os valores digitados são {valores}.')
