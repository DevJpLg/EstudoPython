"""
Criar um programa para calcular as raízes de uma equação de segundo grau.
Inicialmente o programa deverá viabilizar a entrada de valores reais para as
variáveis A, B e C. Em seguida deverá ser calculado o valor de DELTA. Caso o
valor de DELTA seja menor do que 0 o programa deverá informar que não existem
valores reais para as raízes, caso seja 0 deverá informar que existe somente uma
raiz e o seu valor, caso contrário deverão ser informados os valores da raízes.
Fórmula para realizar os cálculos das raízes: Delta = b² - 4ac
"""
import math

valorA = float(input("Digite o valor de 'A': "))
valorB = float(input("Digite o valor de 'B': "))
valorC = float(input("Digite o valor de 'C': "))

delta = (valorB * valorB) - 4*valorA*valorC

if delta < 0:
    print('Não existem valores reais para as raízes!')
elif delta == 0:
    delta = -valorB/(2*valorA)
    print('Só existe um valor para a raiz que é %.2f' % delta)
else:
    resultado_1 = (-valorB + math.sqrt(delta))/(2*valorA)
    resultado_2 = (-valorB - math.sqrt(delta))/(2*valorA)
    print('Primeiro valor: %.1f\nSegundo valor: %.1f' % (resultado_1, resultado_2))