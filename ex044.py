'''Exercício Python 044: Elabore um programa que
calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print(f'{"=====LOJA AMERICANAS====":^10}')
valor = float(input('Digite um valor: '))
print('''

[ 1 ] à vista no dinheiro/cheque.
[ 2 ] à vista no cartão.
[ 3 ] em 2x no cartão, sem juros.
[ 4 ] 3x ou mais no cartão, com juros

''')

num  = int(input('Escolha uma opção: '))
if num == 1:
    s = valor - (valor * 10/100)
    print(f'O valor a ser pago é R$ {s:.2f}')
if num == 2:
    s = valor - (valor * 5/100)
    print(f'O valor a ser pago é R$ {s:.2f}')
if num == 3:
    s = valor / 2
    print(f'O valor da parcela a em 2x é de R$ {s:.2f}.')
if num == 4:
    parcela = int(input('Quantas parcelas você deseja fazer? '))
    n = valor + (valor * 20/100)
    s = n / parcela
    print(f'O valor de cada parcela é de R$ {s:.2f}, contém juros.')


