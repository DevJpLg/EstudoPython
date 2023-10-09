#Dado o peso e a altura do usuário imprima seu Índice de Massa Corporal. 
#IMC = peso / altura 2

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso/(pow(altura, 2))

print('O seu índice de massa corporal (IMC) é de %.2f!' % imc)