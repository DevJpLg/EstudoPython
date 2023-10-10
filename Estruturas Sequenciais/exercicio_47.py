"""
Faça um algoritmo para executar uma pesquisa entre um número de pessoas
determinado pelo usuário. Após a entrada dos devidos dados informe:
- O nome da pessoa mais nova e a sua idade
- O nome da pessoa mais velha e a sua idade
- A média das idades
"""

qtd_pessoas = int(input('Insira o número de participantes para começar a pesquisa: '))

indice = 0
media_idades = 0
pessoa_mais_nova = 999
pessoa_mais_velha = 0
nome_mais_velho = ''
nome_mais_novo = ''

while indice < qtd_pessoas:
    indice += 1
    print('\n****** Pessoa Nº%d ******' % indice)
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    media_idades += idade
    if idade > pessoa_mais_velha:
        pessoa_mais_velha = idade
        nome_mais_velho = nome
    elif idade < pessoa_mais_nova:
        pessoa_mais_nova = idade
        nome_mais_novo = nome
media_idades = media_idades/qtd_pessoas

print('\nA pessoa mais nova é o(a) "%s" com %d anos.' % (nome_mais_novo, pessoa_mais_nova))
print('A pessoa mais velha é o(a) "%s" com %d anos.' % (nome_mais_velho, pessoa_mais_velha))
print('A média de idades é de %d anos.' % media_idades)