"""
Uma determinada companhia deseja obter o resultado de uma pesquisa
relacionada a um novo produto. As respostas dos entrevistados devem ser
apresentadas da seguinte maneira:
- se o cliente gostou será digitada a letra S;
- se o cliente não gostou será digitada será digitada a letra N;
- se não for digitada nem a letra S nem a N, o algoritmo deverá ser finalizado;
Informe:
Bom : se a maior parte dos entrevistados responder sim;
Ruim : se a maior parte dos entrevistados responder não;
Empate : caso ocorra empate;
"""

qtd_pessoas = int(input('Insira o número de participantes para começar a pesquisa: '))

resposta_positiva = 0
resposta_negativa = 0
indice = 0

while indice < qtd_pessoas:
    indice += 1
    print('\n****** Participante Nº%d ******' % indice)
    escolha = input('Você gostou do nosso produto? [S]im [N]ão: ')
    if escolha == 'S' or escolha == 's':
        resposta_positiva += 1
    elif escolha == 'N' or escolha == 'n':
        resposta_negativa += 1
    else:
        print('Reposta inválida!')
        break

print('\n*** Resultado Final ***')
if resposta_negativa < resposta_positiva:
    print('Bom')
elif resposta_negativa > resposta_positiva:
    print('Ruim')
else:
    print('Empate')