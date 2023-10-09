#Leia um número inteiro e imprima o seu antecessor e o seu sucessor

numero = int(input('Digite um número inteiro: '))

antecessor = numero - 1
sucessor = numero + 1

print('O antecessor do número %d é %d!\nO sucessor do número %d é %d!' % (numero, antecessor, numero, sucessor))