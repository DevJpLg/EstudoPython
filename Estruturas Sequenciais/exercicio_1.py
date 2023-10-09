"""
Leia um valor de temperatura em graus Celsius e converta-o em graus Fahrenheit
e Kelvin. A fórmula de conversão é:
F = (9C + 160) / 5
K = C + 273
"""

grausCelsius = int(input('Digite o valor da temperatura em graus Celsius: '))

grausFahrenheit = (((9 * grausCelsius) + 160)/5)
grausKelvin = grausCelsius + 273

print('O valor da conversão em "Fahrenheit" é de %dºF' % grausFahrenheit)
print('O valor da conversão em "Kelvin" é de %dK' % grausKelvin)