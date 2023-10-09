"""
Leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com
30 dias
"""

idade = int(input('Insira a sua idade em anos: '))

idade_meses = idade * 30
idade_dias = idade * 365

print('Idade em anos: %d\nIdade em meses: %d\nIdade em dias: %d' % (idade, idade_meses, idade_dias))