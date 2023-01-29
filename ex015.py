'''Exercício Python 15: Escreva um programa que 
pergunte a quantidade de Km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi 
alugado. Calcule o preço a pagar, sabendo que o carro 
custa R$60 por dia e R$0,15 por Km rodado.'''

dias = km = total = 0

dias_de_alugado = int(input('Digite quantos dias você ficou com o carro: '))
quilometragem = float(input('Digite quantos Km você percorreu com o carro: '))
dias = dias_de_alugado * 60
km = quilometragem * 0.15
total = dias + km

print(
    f'O valor total a ser pago por {dias_de_alugado} dias com o carro e ter percorrido a distancia de {quilometragem:.2f}Km é de R$ {total:.2f}')

