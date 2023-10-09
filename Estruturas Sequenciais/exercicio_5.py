"""
Prepare um algoritmo para calcular o espaço percorrido por um móvel em
movimento retilíneo uniforme dada a seguinte fórmula: S=So+V*T.
Inicialmente o algoritmo deverá perguntar ao usuário os valores do espaço
inicial(So), da velocidade(V) e do tempo(T). Após a entrada dos devidos valores
estes devem ser substituídos na fórmula, resultando assim no espaço percorrido(S)
que deverá ser informado na tela do usuário
"""

espacoInicial = float(input('Digite o valor do espaço inicial (So): '))
velocidade = float(input('Digite o valor da velocidade (V): '))
tempo = float(input('Digite o valor do tempo (T): '))

espacoPercorrido = espacoInicial + (velocidade * tempo)

print('O espaço percorrido (S) foi de %d metros' % espacoPercorrido)