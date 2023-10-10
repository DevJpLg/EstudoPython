"""
Prepare um algoritmo para perguntar a um certo número de pessoas seu nome,
sexo, peso e nacionalidade. Informe:
• A média de peso destas pessoas
• O nome da pessoa mais pesada
• O nome da mulher brasileira mais leve
Parar a execução do algoritmo quando o nome da pessoa for ASTROBALDO
"""

indice = 0
media_peso = 0
pessoa_mais_pesada = 0
mulher_mais_leve = 999
nome_mais_pesado = ''
nome_mais_leve = ''

qtd_pessoas = int(input('Digite a quantidade de pessoas para iniciar as perguntas: '))
while indice < qtd_pessoas:
    indice += 1
    print('\n*****%dª Pessoa*****' % indice)
    nome = input('Digite o seu nome: ')
    if nome == 'ASTROBALDO':
        break
    sexo = input('Digite o seu sexo (M - Masculino e F - Feminino): ')
    peso = float(input('Digite o seu peso em Kg: '))
    nacionalidade = input('Digite a sua nacionalidade: ')
    media_peso += peso
    if (sexo == 'F' or sexo == 'f') and nacionalidade == 'Brasileira':
        if peso < mulher_mais_leve:
            mulher_mais_leve = peso
            nome_mais_leve = nome
    if peso > pessoa_mais_pesada:
        pessoa_mais_pesada = peso
        nome_mais_pesado = nome
media_peso = media_peso/qtd_pessoas
print('\nA média de peso é de %.2f Kg\nA pessoa mais pesada é o(a) "%s"' % (media_peso, nome_mais_pesado))
if nome_mais_leve != '':
    print('A mulher brasileira mais leve é a "%s"' % nome_mais_leve)