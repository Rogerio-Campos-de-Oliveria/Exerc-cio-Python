'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.    

Ex:
    escreva('Olá, Mundo!')
Saída:
    ~~~~~~~~~~~~
     Olá, Mundo!
    ~~~~~~~~~~~~'''
    
def frase (txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


#Programa Principal
texto = str(input('Digite uma frase: '))
frase(texto)