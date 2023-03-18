'''Exercício Python 70: Crie um programa que leia o 
nome e o preço de vários produtos. O programa deverá 
perguntar se o usuário vai continuar ou não. No final, 
mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

maisMIL = menor = total = cont = 0
barto = ' '
while True:
    print('=-=' * 20)
    produto = str(input('Escreva o nome do produto: '))
    preço = float(input(f'Digite o valor do produto {produto}: R$ '))
    
    cont += 1
    total += preço

    if preço > 1000:
       maisMIL += 1 
    
    
    if cont == 1:
        menor = preço
        barto = produto
    else: 
        if menor < menor:
            menor = preço
            barto = produto
            
    print('=-=' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar a cadastradar? [SN]')).upper().strip()[0]
    if resp == 'N':
        break
print('=-=' * 20)
print(f'O total da sua compra foi de R$ {total:.2f}')
print(f'Foram cadastrados {maisMIL} produtos que custam mais do que R$ 1.000,00')
print(f'O produto mais barato foi {barto} que custa R$ {menor:.2f}.')
print('=-=' * 20)
print('Obrigado, volte sempre!')