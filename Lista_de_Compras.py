import os

lista = []
while True:
    print('\n***Selecione uma opção:***')
    opcao_escolhida = input('[i]inserir  [a]pagar  [l]istar:  ')
    if opcao_escolhida == 'i':
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao_escolhida == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar!')
        for indice, valor in enumerate(lista):
            print(indice, valor)
    elif opcao_escolhida == 'a':
        apagar = input('Escolha um índice para apagar: ')
        try:
            indice = int(apagar)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except Exception:
            print('Erro desconhecido')
        except IndexError:
            print('Índice não existe na lista')
    else:
        print('Digite uma letra que seja "i", "a" e "l"!')
        continue
