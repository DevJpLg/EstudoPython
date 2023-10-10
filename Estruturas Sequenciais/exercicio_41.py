"""
Prepare um algoritmo para perguntar o nome e o sexo de 10 pessoas e informar
quantas são homens e quantas são mulheres
"""

indice = 0
mulheres = 0
homens = 0

while indice < 3:
    indice += 1
    nome = input('Digite o %dº nome: ' % indice)
    sexo = input('Digite o seu sexo (M - Masculino e F - Feminino): ')
    if sexo == 'M' or sexo == 'm':
        homens += 1
    elif sexo == 'F' or sexo == 'f':
        mulheres += 1
print('\nHomens: %d\nMulheres: %d' % (homens, mulheres))