"""
Prepare um algoritmo para realizar o cálculo do preço de um serviço de
Consultoria. Seu algoritmo deverá perguntar os seguintes dados e informar o valor
total do serviço:
Tipo de Serviço (Projeto ou Auditoria)
N.º dias trabalhados
N.º de viagens realizadas
Você deve usar a seguinte tabela para calcular o valor dos serviços:
Tipo de Serviço Dia de Trabalho (R$) Cada Viagem (R$)
Projeto                 200,00          1000,00
Auditoria               100,00          1500,00
"""

print('*** Serviço de Consultoria ***')
dias_trabalhados = int(input('Insira o número de dias trabalhados: '))
viagens_realizadas = int(input('Insira o número de viagens realizadas: '))
tipo_de_servico = input('Escolha um tipo de serviço [P]rojeto ou [A]auditoria: ')

if tipo_de_servico == 'P' or tipo_de_servico == 'p':
    valor_do_servico = (dias_trabalhados * 200) + (viagens_realizadas * 1000)
    print('\nO valor total do serviço foi de R$', valor_do_servico)
elif tipo_de_servico == 'A' or tipo_de_servico == 'a':
    valor_do_servico = (dias_trabalhados * 100) + (viagens_realizadas * 1500)
    print('\nO valor total do serviço foi de R$', valor_do_servico)