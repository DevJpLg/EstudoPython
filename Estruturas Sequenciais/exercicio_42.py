"""
Prepare um algoritmo para perguntar o nome, o sexo e a idade de 40 pessoas e
informar:
• a média de idades
• a média de idades dos homens
• o total de mulhere
"""

indice = 0
media = 0
homens = 0
homens_idade = 0
mulheres = 0
media_idades = 0

while indice < 3:
    indice += 1
    nome = input('Digite o %dº nome: ' % indice)
    sexo = input('Digite o seu sexo (M - Masculino e F - Feminino): ')
    idade = int(input('Digite a sua idade em anos: '))
    media_idades += idade
    if sexo == 'M' or sexo == 'm':
        homens += 1
        if idade > 0:
            homens_idade += idade
    elif sexo == 'F' or sexo == 'f':
        mulheres += 1
media_idades = media_idades/40
media_homem = homens_idade/homens
print('\nA média de idades: %d anos\nA média de idades dos homens: %d anos\nO total de mulheres: %d' % (media_idades, media_homem, mulheres))