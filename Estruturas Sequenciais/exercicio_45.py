"""
Prepare um algoritmo para controlar as informações sobre utilização de um banco
eletrônico. Seu algoritmo deverá perguntar a 1000 clientes qual foi a operação que
eles realizaram. Os tipos válidos são:
- Retirada
- Depósito
- Extrato
- Transferência
Informe quantas operações foram efetuadas de cada tipo.
"""

indice = 0
retirada = 0
deposito = 0
extrato = 0
transferencia = 0

while indice < 1000:
    indice += 1
    print('\n****** Cliente Nº%d ******' % indice)
    print('\n1 - Retirada\n2 - Depósito\n3 - Extrato\n4 - Transferência\n')
    escolha = int(input('Digite um número para começar: '))
    if escolha == 1:
        print('\nOpção selecionada: "Retirada"')
        retirada += 1
    elif escolha == 2:
        print('\nOpção selecionada: "Depósito"')
        deposito += 1
    elif escolha == 3:
        print('\nOpção selecionada: "Extrato"')
        extrato += 1
    elif escolha == 4:
        print('\nOpção selecionada: "Transferência"')
        transferencia += 1
    else:
        print('\nOpção inválida!\nAbortando...')
        break
print('\n******Número de operações efetuadas******')
print('Retirada: %d' % retirada)
print('Depósito: %d' % deposito)
print('Extrato: %d' % extrato)
print('Transferência: %d' % transferencia)