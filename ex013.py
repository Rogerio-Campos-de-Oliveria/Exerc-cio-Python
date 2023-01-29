'''Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

nome_funcionario = str(input('Digite o nome do funcionário: '))
salário_funcionario = float(input(f'Digite o salário do funcionário {nome_funcionario} R$ '))
salario_ajustado = salário_funcionario + salário_funcionario * 15 / 100
print(f'O salários do funcionário {nome_funcionario} foi reajustodo com 15% de aumento e agora o seu salário atual é de R$ {salario_ajustado:.2f}.')
