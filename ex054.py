'''Exercício Python 54: Crie um programa que leia o 
ano de nascimento de sete pessoas. No final, mostre 
quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores.'''

from datetime import date
data_atual = date.today().year
maior = menor = tot =0
for c in range(1, 8):
    nasc = int(input(f'Digite a data de nascimento da {c}° pessoa:[aaaa]  '))
    ano = data_atual - nasc

    if ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos \33[33m{maior} \033[mpessoas maiores de idade e \33[31m{menor} \33[mpessoas menores de idade.')
