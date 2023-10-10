#Prepare um algoritmo para perguntar 40 números e informar o maior e o menor número lido

indice = 0
maior_Numero = 0

while indice < 40:
    indice += 1
    numero = int(input('Digite o %dº número: ' % (indice)))
    if numero >= maior_Numero:
        maior_Numero = numero
print('\nO maior número é:', maior_Numero)