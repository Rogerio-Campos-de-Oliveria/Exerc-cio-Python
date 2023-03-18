'''Exercício Python 64: Crie um programa que leia 
vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles 
(desconsiderando o flag).'''

saldo = núm = 0
cont = 0

while núm != 999:
    núm = int(input('Digite um número [para encerrar digite 999]: '))
    if núm != 999:
        saldo = saldo + núm
        cont += 1
print(f'Você digitou o total de {cont} e a soma dos valores foi de {saldo}.')
print('Fim do programa !!!')