"""
Prepare um algoritmo para perguntar o nome e a altura de 20 pessoas e informar a
média destas alturas, a altura da pessoa mais baixa e o nome da pessoa mais alta
"""

indice = 0
altura_mais_alta = 0
altura_mais_baixa = 999
nome_mais_alto = ''

while indice < 20:
    indice += 1
    print('\n***%dº Pessoa***' % indice)
    nome = input('Digite o seu nome: ')
    altura = float(input('Digite a sua altura: '))
    if altura < altura_mais_baixa:
        altura_mais_baixa = altura
    if altura > altura_mais_alta:
        altura_mais_alta = altura
        nome_mais_alto = nome
    altura += altura
soma_alturas = altura/20
print('\nA média das alturas é de: %.2f metros\nA altura da pessoa mais baixa é de: %.2f metros\nO nome da pessoa mais alta é: "%s"' % (altura, altura_mais_baixa, nome_mais_alto))