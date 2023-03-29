'''Exercício Python 078: Faça um programa que leia 5
valores numéricos e guarde-os em uma lista. No 
final, mostre qual foi o maior e o menor valor 
digitado e as suas respectivas posições na lista.'''

núm = list()
maior = menor = 0
for c in range(0,5):
    núm.append(int(input(f'Digite um número inteiro na posição {c}: ')))
    if c == 0:
        maior = menor = núm[c]
    else:
        if núm[c] > maior:
            maior = núm[c]
        if núm[c] < menor:
            menor = núm[c]
    
print('=-=' * 20)
print(f'Você digitou os valores {núm}.')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(núm):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(núm):
    if v == menor:
        print(f'{i}... ', end='')
print()
