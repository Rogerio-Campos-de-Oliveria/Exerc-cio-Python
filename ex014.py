'''Exercício Python 14: Escreva um programa que 
converta uma temperatura digitando em graus Celsius e 
converta para graus Fahrenheit.'''

temperatura = float(input('Digite a temperatura em Celsius: '))
farenheint = (temperatura * 1.8) + 32
print(f'A temperatura convertidade de {temperatura:.2f}°C Celsius para Firenheint é de {farenheint:.2f}°F.')