import os

lista_compras = []

while True:
    
    print('\n(1)Adicionar um item (2)Remover um item (3)Visualizar lista (4)Sair')

    try:
        opcao = int(input('Escolha uma das opções acima: '))
    except ValueError:
        print('Digite um número válido! Ex: 1, 2, 3 ou 4.')
        continue  # Volta pro início do while 

    if opcao == 1:

        os.system('cls')
        item = input('Digite um item: ')
        lista_compras.append(item)

    elif opcao == 2:

        os.system('cls')
        if not lista_compras:
            print('A lista está vazia.')
            continue

        for indice, nome in enumerate(lista_compras):
            print(f'{indice} - {nome}')

        try:

            excluir = int(input('Digite o indice do item que deseja remover: '))

            if 0 <= excluir < len(lista_compras):
                removido = lista_compras.pop(excluir)
            
                print(f'O item {removido} foi removido.')

            else:
                print('Índice inválido')

        except ValueError:
            print('Digite um indice válido:')
        except IndexError:
            print('Indice não existente:')
        except Exception:
            print('Erro desconhecido')
    
    elif opcao == 3:

        if lista_compras:
            print('Lista de compras:')
            for item in lista_compras:
                print(f'- {item}')
        else:
            print('A lista está vazia')
    
    elif opcao == 4:
        print('Saindo...')
        break

    else:
        print('Opção inválida')





