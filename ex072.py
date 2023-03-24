'''Exercício Python 72: Crie um programa que tenha uma dupla 
totalmente preenchida com uma contagem por extenso, de zero até 
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
e mostrá-lo por extenso.'''

números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

  
while True:
    escolhido = int(input('Digite um número de 0 a 20: '))
    if 0 <= escolhido <= 20:
        break
    print('Tente novamente. ',end= ' ')
print(f'O número que você escolhei foi {números[escolhido]}.')
print('=-=' * 20) 
print('Obrigado, volte sempre!')
print('=-=' * 20)      