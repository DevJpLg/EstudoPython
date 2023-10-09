"""
Tendo como dados de entrada a altura o sexo e o peso de uma pessoa, construa
um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
. Para homens: (72.7*h) - 58
. Para mulheres: (62.1*h) - 44.7 (h = altura)
Informe se o peso da pessoa está dentro, acima ou abaixo do peso
(Considere a margem de erro de 1 Kg para mais ou para menos como estando no
peso ideal).
"""

altura = float(input('Digite a sua altura em metros: '))
sexo = input('Digite o seu sexo [F]eminino ou [M]asculino: ')
peso = float(input('Digite o seu peso em kg: '))

if sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1 * altura) - 44.7
    print('Peso ideal: %.2f' % pesoIdeal)
elif sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7 * altura) - 58
    print('Peso ideal: %.2f' % pesoIdeal)
else:
    print('Sexo inválido!')
if peso > pesoIdeal + 1:
    print('Você está acima do peso ideal!')
elif peso < pesoIdeal - 1:
    print('Você está abaixo do peso ideal!')
else:
    print('Você está dentro do peso ideal!')