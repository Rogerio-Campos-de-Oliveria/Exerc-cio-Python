'''Exercício Python 33: Faça um programa que leia três 
números e mostre qual é o maior e qual é o menor.'''

n = 0
valores = list()
for c in range(0, 3):
    número = float(input('Digite um valor: '))
    valores.append(número)
print(valores)
# Analisando o MAIOR valor
maior = valores[0]
if valores[1] > valores[0] and valores[1] > valores[2]:
    maior = valores[1]
if valores[2] > valores[1] and valores[2] > valores[0]:
    maior = valores[2]
    
# Analisando o MENOR valor
menor = valores[0]
if valores[1] < valores[0] and valores[1] < valores[2]:
    menor = valores[1]
if valores[2] < valores[1] and valores[2] < valores[0]:
    menor = valores[2]
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
