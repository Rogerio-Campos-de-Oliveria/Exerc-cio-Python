'''Exercício Python 038: Escreva um programa que 
leia dois números inteiros e compare-os. mostrando 
na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

número_01 = int(input('Digite o primeiro número inteiro: '))
número_02 = int(input('Digite o segundo número inteiro: '))
if número_01 > número_02:
    print(f'O número {número_01} é maior que o número {número_02}')
elif número_01 < número_02:
    print(f'O número {número_02} é maior que o número {número_01}')
else:
    print(f'Os número são iguais.')
    