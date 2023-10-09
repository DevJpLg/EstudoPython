"""
Leia o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e
escrever o valor do novo salário
"""

salario_mensal = float(input('Insira o salário mensal do funcionário: '))
reajuste = float(input('Digite o percentual de reajuste: '))

salario_novo = salario_mensal + (salario_mensal * (reajuste * 0.01))

print('O novo salário do funcionário será de R$', salario_novo)