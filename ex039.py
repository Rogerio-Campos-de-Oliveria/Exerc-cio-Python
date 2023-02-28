'''Exercício Python 39: Faça um programa que leia o 
ano de nascimento de um jovem e informe, de acordo 
com a sua idade, se ele ainda vai se alistar ao 
serviço militar, se é a hora exata de se alistar ou 
se já passou do tempo do alistamento. Seu programa 
também deverá mostrar o tempo que falta ou que 
passou do prazo.'''

from datetime import date
ano_atual = date.today().year
nasc = int(input('Digite a ano que você nasceu: '))
idade = ano_atual - nasc
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}.')
    