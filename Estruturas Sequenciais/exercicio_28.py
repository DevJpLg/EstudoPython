"""
Preparar um algoritmo para ler os comprimentos dos três lados de um triângulo
(A,B e C) e determinar que tipo de triângulo temos, com base nos seguintes casos:
 - Se A>=B+C nenhum triângulo é formado
 - Se A2 = B2 + C2 um triângulo retângulo é formado
 - Se A2 > B2 + C2 um triângulo obtusângulo é formado
 - Se A2 < B2 + C2 um triângulo acutângulo é formado
"""

lado_A = float(input('Digite o lado A do triângulo: '))
lado_B = float(input('Digite o lado B do triângulo: '))
lado_C = float(input('Digite o lado C do triângulo: '))

if lado_A >= lado_B + lado_C:
    print('\nNenhum lado é formado!')
elif pow(lado_A, 2) == pow(lado_B, 2) + pow(lado_C, 2):
    print('\nUm triângulo retângulo é formado')
elif pow(lado_A, 2) > pow(lado_B, 2) + pow(lado_C, 2):
    print('\nUm triângulo obtusângulo é formado')
elif pow(lado_A, 2) < pow(lado_B, 2) + pow(lado_C, 2):
    print('\nUm triângulo acutângulo é formado')