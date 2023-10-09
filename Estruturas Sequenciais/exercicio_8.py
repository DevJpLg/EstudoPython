"""
Implemente um programa que lê três valores e calcule a média ponderada para
pesos 1, 2 e 3, respectivamente (multiplique cada nota pelo seu peso, some os
produtos e divida o resultado pela soma dos pesos).
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media_ponderada = ((nota1 * 1) + (nota2 * 2) + (nota3 * 3))/6

print('A média das notas é de %.2f' % media_ponderada)