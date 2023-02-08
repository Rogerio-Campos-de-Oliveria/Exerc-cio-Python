'''Exercício Python 27: Faça um programa que leia o nome 
completo de uma pessoa, mostrando em seguida o primeiro e o 
último nome separadamente.'''

nome = str(input('Digite seu nome: '))
divisão = nome.split()
print(f'Seu primeiro nome é {divisão[0]}')
print(f'Seu último nome é {divisão[len(divisão)-1]}')
