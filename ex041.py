'''Exercício Python 041: A Confederação Nacional de 
Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de 
acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
data_atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta (aaaa): '))
idade = data_atual - nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos e está na categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos e está na categoria JÚNIOR.')
elif 19 < idade <= 25:
    print(f'O atleta tem {idade} anos e está na categoria SÊNIOR.')
elif idade > 25:
    print(f'O atleta tem {idade} anos e está na categoria MASTER.')