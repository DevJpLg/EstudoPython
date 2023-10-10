"""
Prepare um algoritmo para calcular a soma dos números entre 1 e N inclusive. O
valor de N deve ser perguntado no início do algoritmo
"""

numero = int(input('Digite um número: '))
indice = 0
soma = 0

for indice in range(numero):
    soma += indice + 1
print('A soma dos números entre 1 e %d é %d' % (numero, soma))