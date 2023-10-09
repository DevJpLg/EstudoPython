"""
Escrever um algoritmo que leia um valor e calcule qual o menor número possível
de notas e moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido pode ser
decomposto. Escrever o valor lido e a relação de notas necessárias
"""

valor = int(input('Insira um valor: '))

notas100 = valor // 100
valor %= 100
notas50 = valor // 50
valor %= 50
notas20 = valor // 20
valor %= 20
notas10 = valor // 10
valor %= 10
notas5 = valor // 5
valor %= 5
notas2 = valor // 2
valor %= 2
moedas1 = valor

print("Notas de 100:", notas100)
print("Notas de 50:", notas50)
print("Notas de 20:", notas20)
print("Notas de 10:", notas10)
print("Notas de 5:", notas5)
print("Notas de 2:", notas2)
print("Moedas de 1:", moedas1)