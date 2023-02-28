'''Exercício Python 36: Escreva um programa para 
aprovar o empréstimo bancário para a compra de uma 
casa. Pergunte o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar. A 
prestação mensal não pode exceder 30% do salário ou 
então o empréstimo será negado.'''

valor_casa = float(input('Digite o calor da casa: R$ '))
salário = float(input('Qual é o valor do seu salário: R$ '))
prazo = int(input('Enquanto anos você quer pagar  sua casa? '))
meses = prazo * 12
prestação = valor_casa / meses
if prestação <= 30 / 100 * salário:
    print('Financiamento aprovado.')
else:
    print('Financiamento negado.')
