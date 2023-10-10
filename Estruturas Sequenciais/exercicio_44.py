"""
Faça um programa de menu que mostra na tela, sob o título de "Menu Principal",
três opções: "1 - Fim", "2 - Cadastro" e "3 - Consulta", lê do teclado a opção
desejada pelo usuário e mostra uma mensagem confirmando a opção escolhida ou
uma mensagem de erro, se a opção for inválida.
"""

while True:
    print('\n****** Menu Principal ******')
    print('\n1 - Fim\n2 - Cadastro\n3 - Consulta')
    escolha = int(input('Digite um número para começar: '))
    if escolha == 1:
        print('\nOpção selecionada: "Fim"')
    elif escolha == 2:
        print('\nOpção selecionada: "Cadastro"')
    elif escolha == 3:
        print('\nOpção selecionada: "Consulta"')
    else:
        print('\nOpção inválida!\nAbortando...')
        break