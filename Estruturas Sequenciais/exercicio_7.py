"""
Prepare um programa para informar o total gasto em uma lavanderia. O algoritmo
inicialmente deverá perguntar o total de camisas, o total de calças e o total de
meias e informar o total gasto, levando em conta a seguinte tabela de preços:
Camisas : 5.00 Calças :10.00 Meias :2.00
"""

total_camisas = int(input('Insira o total de camisas: '))
total_calcas = int(input('Insira o total de calças: '))
total_meias = int(input('Insira o total de meias: '))

total_gasto = (total_camisas * 5) + (total_calcas * 10) + (total_meias * 2)

print('O total gasto será de R$', total_gasto)