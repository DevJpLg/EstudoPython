"""
Prepare um algoritmo para realizar o cálculo do salário de uma pessoa. Seu
algoritmo deverá perguntar os seguintes dados sobre o empregado:
Cargo (Gerente, Supervisor, Auxiliar)
N.º Horas Extras trabalhadas
N.º de Faltas
N.º de Filhos
Você deve usar a seguinte tabela para calcular o valor dos salários:
Tipo de Empregado Salário Base
Gerente             2000,00
Supervisor          900,00
Auxiliar            300,00
Cada hora extra vale (Salário Base /240) * 2
Cada Falta custa: Salário Base /30
Cada Filho vale: 3% do salário base
INSS = 10% dos Proventos
Proventos = (salario base + horas extras + adicional por filhos)
Descontos = (Faltas + INSS)
Salário Líquido = Proventos - Descontos
Leia os dados e informe o total de Proventos, Descontos e o Salário Líquido
"""

def calcular_salario(cargo, qtd_hora_extra, qtd_faltas, qtd_filhos):
    if cargo == 'G':
        salario_base = 2000
    elif cargo == 'S':
        salario_base = 900
    elif cargo == 'A':
        salario_base = 300
    else:
        return "Cargo inválido!"
    valor_hora_extra = (salario_base / 240) * 2 * qtd_hora_extra
    valor_falta = salario_base / 30 * qtd_faltas
    valor_filho = salario_base * (qtd_filhos * 0.03)
    proventos = (salario_base + valor_hora_extra + valor_filho)
    inss = 0.10 * proventos
    descontos = valor_falta + inss
    salario_liquido = proventos - descontos
    return proventos, descontos, salario_liquido

qtd_hora_extra = int(input('Insira as suas horas trabalhadas: '))
qtd_faltas = int(input('Insira a quantidade de faltas: '))
qtd_filhos = int(input('Insira a quantidade de filhos: '))
cargo = input('Digite o seu cargo:\n[G]erente, [S]upervisor, [A]uxiliar: ')

proventos, descontos, salario_liquido = calcular_salario(cargo, qtd_hora_extra, qtd_faltas, qtd_filhos)

print("Proventos: R$ %.2f" % proventos)
print("Descontos: R$ %.2f" % descontos)
print("Salário líquido: R$ %.2f" % salario_liquido)