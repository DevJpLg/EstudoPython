#Construa um programa que receba a idade do usuário e verifique se ele tem mais de 21 anos.

idade = int(input('Digite a sua idade: '))

if idade > 21:
    print('Você tem mais de 21 anos!')
elif idade == 21:
    print('Você tem 21 anos!')
else:
    print('Você não tem 21 anos ou mais!')