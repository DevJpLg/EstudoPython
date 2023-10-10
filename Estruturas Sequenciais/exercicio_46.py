"""
Faça um algoritmo para simular uma situação simples de depósito, retirada e
consulta em um banco.
O algoritmo inicialmente deverá mostrar um menu com as seguintes opções:
1 - Depósito
2 - Retirada
3 - Saldo
4 - Sair do algoritmo
Se a escolha do usuário for depósito ou retirada, o algoritmo deverá pedir o valor
da operação e atualizar automaticamente o valor existente na conta.
O algoritmo deverá ser utilizado até que o usuário escolha a opção sair do
algoritmo.
"""

saldo = 0

while True:
    print('\n***Menu Principal***')
    print('\n1 - Depósito\n2 - Retirada\n3 - Saldo\n4 - Sair do algoritmo')
    escolha = int(input('Digite um número para começar: '))
    if escolha == 1:
        valor_inserido_deposito = float(input('Digite o valor do depósito: '))
        saldo += valor_inserido_deposito
        print('\nVocê depositou R$ %.2f' % valor_inserido_deposito)
    elif escolha == 2:
        valor_inserido_retirada = float(input('Digite o valor da retirada: '))
        if valor_inserido_retirada <= saldo:
            saldo = saldo - valor_inserido_retirada
            print('\nVocê retirou R$ %.2f' % valor_inserido_retirada)
        else:
            print('\nNão é possível retirar o valor de R$ %.2f, pois o seu saldo atual é de R$ %.2f' % (valor_inserido_retirada, saldo))
    elif escolha == 3:
        print('\nSaldo atual: R$ %.2f' % saldo)
    elif escolha == 4:
        break
    else:
        print('\nNúmero inválido!')