"""
Faça um programa que peça para entrar com um ano com 4 dígitos 
e determine se o mesmo é ou não bissexto.

De 4 em 4 anos é ano bissexto.
De 100 em 100 anos não é ano bissexto.
De 400 em 400 anos é ano bissexto.

"""

ano_inserido = int(input('Digite um ano com 4 dígitos: '))

if (ano_inserido % 4 == 0 and ano_inserido % 100 != 0) or ano_inserido % 400 == 0:
    print('O ano %d é bissexto!' % ano_inserido)
else:
    print('O ano %d não é bissexto!' % ano_inserido)