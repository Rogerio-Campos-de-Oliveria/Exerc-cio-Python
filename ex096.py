'''Exercício Python 096: Faça um programa que tenha uma 
função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a 
área do terreno.'''

def area (l, c):
    soma = c * l
    print('=-=' * 20)
    print(f'A área de um terro {l}m x {c}m é de {soma}m².')
    print()

#Programa Principal    
print('=-=' * 20)
print('Controle de Terreno')
print('=-=' * 20)

l = float(input('Digite a largura(m): '))
c = float(input('Digite o comprimento(m): '))
area(l, c)