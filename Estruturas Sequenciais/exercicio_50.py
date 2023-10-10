"""
Faça um algoritmo para calcular a área de figuras geométricas. Inicialmente o
algoritmo deverá apresentar ao usuário um menu principal, onde será escolhida
uma dentre as seguintes opções:
1 - Calcular a área do quadrado
2 - Calcular a área do retângulo
3 - Calcular a área do triângulo
4 - Calcular a área do círculo
5 - Sair do algoritmo
 Após ser escolhida uma das figuras, o usuário deverá então entrar com as devidas
medidas da mesma para que o cálculo possa ser realizado.
Depois de informar o resultado do cálculo, o algoritmo deverá então voltar ao menu
principal até que o usuário deseje finalizar o algoritmo.
"""

while True:
    print('\n***** Menu Principal *****')
    print('1 - Calcular a área do quadrado\n2 - Calcular a área do retângulo\n3 - Calcular a área do triângulo\n4 - Calcular a área do círculo\n5 - Sair do algoritmo')
    escolha = int(input('Digite um número para começar: '))
    if escolha == 1:
        print('\n*** Área do quadrado ***')
        lado = float(input('Digite o lado do quadrado: '))
        area_quadrado = lado * lado
        print('\nÁrea do quadrado:', area_quadrado)
    elif escolha == 2:
        print('\n*** Área do retângulo ***')
        comprimento = float(input('Digite o comprimento do retângulo: '))
        largura = float(input('Digite o largura do retângulo: '))
        area_retangulo = comprimento * largura
        print('\nÁrea do retângulo:', area_retangulo)
    elif escolha == 3:
        print('\n*** Área do triângulo ***')
        base = float(input('Digite a base do triângulo: '))
        altura = float(input('Digite a altura do triângulo: '))
        area_triângulo = (base * altura) / 2
        print('\nÁrea do triângulo:', area_triângulo)
    elif escolha == 4:
        print('\n*** Área do círculo ***')
        raio = float(input('Digite o raio do círculo: '))
        area_círculo = 3.1415 * (raio * raio)
        print('\nÁrea do círculo:', area_círculo)
    elif escolha == 5:
        break
    else:
        print('\nNúmero inválido!')