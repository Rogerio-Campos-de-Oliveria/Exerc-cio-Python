'''Exercício Python 43: Desenvolva uma lógica que 
leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

#Dados para o calculo
peso = float(input('Digite seu peso em Kg: '))

altura = float(input('Digite sua altura em m, cm: '))

#Caso a pessoa não coloque a postuação na altura, vai calcular sem mostrar para o usuário
if altura.is_integer():
    altura = altura / 100

#calculo do IMC
imc = peso / (altura) ** 2

#Resultado Demonstrar na Tela
print(f'Seu IMC é de {imc}.')
if imc < 18.5:
    print('Você está com IMC Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Você está com IMC Peso Ideal.')
elif 25 <= imc < 30:
    print('Você está com IMC Sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com IMC Obesidade.')
elif imc > 40:
    print('Você está com IMC Obesidade Mórbida.')