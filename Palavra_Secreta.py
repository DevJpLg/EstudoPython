import os

while True:
    palavra_secreta = input('\nDigite uma palavra secreta: ')
    os.system('cls')
    numero_tentativas = 0
    letras_acertadas = ''
    palavra_formada = ''
    while palavra_formada != palavra_secreta:
        letra_digitada = input('\nDigite uma letra: ')
        numero_tentativas += 1
        if len(letra_digitada) > 1:
            print('Digite apenas uma letra.')
            continue
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print('Palavra formada:', palavra_formada)
        if palavra_formada == palavra_secreta:
            os.system('cls')
            print('\nVOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era:', palavra_secreta)
            print('Número de tentativas:', numero_tentativas)