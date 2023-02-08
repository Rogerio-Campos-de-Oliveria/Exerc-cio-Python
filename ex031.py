'''Exercício Python 31: Desenvolva um programa que pergunte a 
distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
parta viagens mais longas.'''

valor = 0
viagem = float(input('Digita a quilometragem da viagem que você vai fazer: '))
if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print(f'Sua viagem de {viagem:.0f} irá custar R$ {valor:.2f}.')
