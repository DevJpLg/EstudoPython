#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

valor = int(input('Digite um valor para saber se ele é positivo ou negativo: '))

if valor >= 0:
    print('O valor %d é positivo!' % valor)
else:
    print('O valor %d é negativo!' % valor)