"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido. Obs: O programa deve
funcionar para letras maiúsculas e minúsculas.
"""

sexo = input('Digite o seu sexo [F]eminino ou [M]asculino: ')

if sexo == 'F' or sexo == 'f':
    print('Sexo escolhido: Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Sexo escolhido: Masculino')
else:
    print('Sexo Inválido!')