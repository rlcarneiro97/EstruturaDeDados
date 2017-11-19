from biblioFila import *

filaNomes = []
opcao = 0

while opcao != 7:
    print('--------------- Fila em Pyhton ---------------\n')
    print(filaNomes)
    print('\n1 - Inserir elemento no fim da fila')
    print('2 - Inserir elemento em posicao especifica')
    print('3 - Alterar elemento especifico da fila')
    print('4 - Excluir elemento do fim da fila')
    print('5 - Excluir elemento de um lugar especifico da fila')
    print('6 - Verificar posicao da pessoa na fila')
    print('7 - Sair')

    while True:
        try:
            opcao = int(input('\nOpção desejada: '))
            break
        except ValueError:
            print('\nOcorreu um erro! Digite novamente!\n')

    if opcao == 1:
        biblioFila.insert(filaNomes)

    if opcao == 2:
        biblioFila.insertEspecific(filaNomes)

    if opcao == 3:
        biblioFila.alter(filaNomes)

    if opcao == 4:
        biblioFila.delete(filaNomes)

    if opcao == 5:
        biblioFila.deleteEspecific(filaNomes)

    if opcao == 6:
        biblioFila.position(filaNomes)