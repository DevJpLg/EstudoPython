"""
Prepare um programa para perguntar dois números e informar qual deles é o maior
ou se os números são iguais.
"""

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))

if numero_1 > numero_2:
    print('O primeiro número "%d" é maior que o segundo número "%d".' % (numero_1, numero_2))
elif numero_1 < numero_2:
    print('O segundo número "%d" é maior que o primeiro número "%d".' % (numero_2, numero_1))
else:
    print('Ambos os números são iguais!')