#Faça a multiplicação entre dois números usando somente soma.

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
indice = 0
resultado = 0

for indice in range(segundo_numero):
    resultado += primeiro_numero
print('\nO resultado da multiplicação é:', resultado)