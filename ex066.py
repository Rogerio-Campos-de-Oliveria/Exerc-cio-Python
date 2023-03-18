'''Exercício Python 66: Crie um programa que leia 
números inteiros pelo teclado. O programa só vai parar 
quando o usuário digitar o valor 999, que é a condição 
de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre elas (desconsiderando 
o flag).'''

soma = cont = 0
while True:
    núm = int(input('Digite um número [999 para parar]: '))
    if núm == 999:
        break
    cont += 1
    soma += núm
print(f'Você digitou {cont} e a soma dos valores foi {soma}!')
