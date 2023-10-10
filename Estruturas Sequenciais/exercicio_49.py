"""
Uma certa firma fez uma pesquisa de mercado para saber se as pessoas gostaram
ou não de um novo produto lançado no mercado. Para isso, cadastrou o sexo do
entrevistado e sua resposta (sim ou não). Sabendo-se que foram entrevistadas
2.000 pessoas, fazer um algoritmo que calcule e escreva:
∙ o número de pessoas que responderam sim;
∙ o número de pessoas que responderam não;
∙ a porcentagem de pessoas do sexo feminino que responderam sim;
∙ a porcentagem de pessoas do sexo masculino que responderam não
"""

indice = 0
resposta_positiva = 0
resposta_negativa = 0
sexo_masculino_negativo = 0
sexo_feminino_positivo = 0

while indice < 2:
    indice += 1
    print('\n****** Participante Nº%d ******' % indice)
    sexo = input('Digite o seu sexo (M - Masculino F - Feminino): ')
    resposta = input('Você gostou do nosso produto? (Sim ou Não): ')
    if resposta == 'Sim' or resposta == 'sim':
        resposta_positiva += 1
        if sexo == 'F' or sexo == 'f':
            sexo_feminino_positivo += 1
    elif resposta == 'Não' or resposta == 'não':
        resposta_negativa += 1
        if sexo == 'M' or sexo == 'm':
            sexo_masculino_negativo += 1

porcentagem_feminino_positivo = (sexo_feminino_positivo/resposta_positiva) * 100
porcentagem_masculino_negativo = (sexo_masculino_negativo/resposta_negativa) * 100

print("\n*****Resultados da pesquisa:*****")
print("Número de pessoas que responderam sim: ", resposta_positiva)
print("Número de pessoas que responderam não: ", resposta_negativa)
print("Porcentagem de pessoas do sexo feminino que responderam sim: ", porcentagem_feminino_positivo, "%")
print("Porcentagem de pessoas do sexo masculino que responderam não: ", porcentagem_masculino_negativo, "%")
