'''Exercício Python 011: Faça um programa que leia 
a largura e a altura de uma parede em metros, calcule 
a sua área e a quantidade de tinta necessária para 
pintá-la, sabendo que cada litro de tinta pinta 
uma área de 2 metros quadrados.'''

largura = comprimento = total = 0
largura = float(input('Digite a largura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
total = largura * comprimento
tinta = total / 2
print(f'Em relação a parede com largura {largura:.2f}m x comprimento {comprimento:.2f}m sua área total é de {total:.2f}m².')
print(f'O total de tinta a ser gasto com a parede é de {tinta:.2f} litros.')
