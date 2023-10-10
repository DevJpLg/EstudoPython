"""
Se tivermos uma lista dos números naturais menores do que 10 que são múltiplos
de 3 ou 5 obtemos 3, 5, 6 e 9. A soma destes múltiplos é 23. Imprima a soma dos
múltiplos de 3 ou 5 menores do que 1000.
"""

numero_digitado = int(input('Digite um número: '))
soma = 0
if numero_digitado < 1000:
    for indice in range(numero_digitado):
        if indice % 3 == 0 or indice % 5 == 0:
            soma += indice
print('A soma dos múltiplos é', soma)