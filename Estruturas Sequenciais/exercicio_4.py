"""
Faça um algoritmo para ler valores para as variáveis A e B, e efetuar a troca dos
valores de forma que, a variável A passe a possuir o valor da variável B e que a
variável B passe a possuir o valor da variável A. Apresentar os valores trocados
"""

valorA = int(input('Digite o valor de A: '))
valorB = int(input('Digite o valor de B: '))

valorAuxiliar = valorA
valorA = valorB
valorB = valorAuxiliar

print('O valor de A é %d\nO valor de B é %d' % (valorA, valorB))