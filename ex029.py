'''Exercício Python 29: Escreva um programa que leia a 
velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma 
mensagem dizendo que ele foi multado. A multa vai custar 
R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual é a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você foi multado por ultrapassar a velocidade 80km/h. Sua multa é de R$ {multa:.2f}.')
print('Boa a viagem! Dirija com segurança.')
