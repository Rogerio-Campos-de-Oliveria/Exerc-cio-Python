'''Exercício Python 34: Escreva um programa que pergunte o 
salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 
10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual é o salário do funcionário: R$ '))
if salario > 1250:
    total = salario + salario * 10 /100
else:
    total = salario + salario * 15 / 100
print(f'O novo salário do funcionário é R$ {total:.2f}.')
    