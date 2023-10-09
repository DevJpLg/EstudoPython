"""
Uma criança quer saber qual é a soma de todas as idades que ela já teve. Elaborar
programa que lê uma idade qualquer e responde rapidamente a essa pergunta
(fórmula para calcular a soma dos N primeiros números inteiros: N (N+1)/2 ).
"""

idade = int(input('Digite a sua idade: '))

idade = ((idade*(idade+1))/2)

print('A soma de todas as idades é de %d anos!' %  idade)