"""
Faça um programa que escreva todos os números múltiplos de 7 entre 1 e N,
sendo N um valor introduzido pelo utilizador. Por exemplos: 7, 14, 21, 28, 35.
"""

numero_digitado = int(input('Digite um número: '))
for indice in range(1, numero_digitado+1):
    if indice % 7 == 0:
        print(indice)