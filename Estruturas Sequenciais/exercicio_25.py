#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

verificar_letra = input('Digite uma letra: ')

vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if verificar_letra in vogal:
    print('A letra "%c" é uma vogal!' % verificar_letra)
elif verificar_letra != vogal:
    print('A letra "%c" é uma consoante!' % verificar_letra)