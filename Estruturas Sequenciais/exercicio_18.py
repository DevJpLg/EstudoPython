"""
Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das
seguintes categorias: infantil A = 5-7 anos; infantil B = 8-10 anos; juvenil A = 11-13
anos; juvenil B = 14-17 anos; adulto = maiores de 18 anos
"""

idade = int(input('Digite a sua idade: '))

if 5 <= idade <= 7:
    print('Categoria: infantil A')
elif 8 <= idade <= 10:
    print('Categoria: infantil B')
elif 11 <= idade <= 13:
    print('Categoria: juvenil A')
elif 14 <= idade <= 17:
    print('Categoria: juvenil B')
elif idade >= 18:
    print('Categoria: adulto')
else:
    print('Você não possui idade suficiente!')