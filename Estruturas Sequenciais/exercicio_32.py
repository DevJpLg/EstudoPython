""""
Prepare um algoritmo para perguntar 10 números e informar a soma total destes
números.
"""

indice = 0
soma = 0
while indice < 10:
    numero = int(input('Digite o %dº número: ' % (indice+1)))
    soma += numero
    indice += 1
print('A soma dos números é:', soma)