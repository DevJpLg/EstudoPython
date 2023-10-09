""""
Faça um Programa que peça o comprimento a largura e a altura de uma caixa
d'água retangular.
Calcule e informe o volume da caixa
"""

print("***Calcular o Volume de uma caixa d'água***")
comprimento = float(input('Insira valor do comprimento da caixa: '))
largura = float(input('Insira valor da largura da caixa: '))
altura = float(input('Insira valor da altura da caixa: '))

volume = comprimento * largura * altura

print("O volume da caixa d'água é de %.2f" % volume)