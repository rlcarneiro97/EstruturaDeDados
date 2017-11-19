from biblioLista import *

listaNomes = []
opcao = 0

while opcao != 7:
    print('--------------- Lista em Pyhton ---------------\n')
    print(listaNomes)
    print('\n1 - Inserir elemento no fim da lista')
    print('2 - Inserir elemento em posicao especifica')
    print('3 - Alterar elemento especifico da lista')
    print('4 - Excluir elemento do fim da lista')
    print('5 - Excluir elemento de um lugar especifico da lista')
    print('6 - Verificar posicao da pessoa na lista')
    print('7 - Sair')

    while True:
        try:
            opcao = int(input('\nOpção desejada: '))
            break
        except ValueError:
            print('\nOcorreu um erro! Digite novamente!\n')

    if opcao == 1:
        biblioLista.insert(listaNomes)

    if opcao == 2:
        biblioLista.insertEspecific(listaNomes)

    if opcao == 3:
        biblioLista.alter(listaNomes)

    if opcao == 4:
        biblioLista.delete(listaNomes)

    if opcao == 5:
        biblioLista.deleteEspecific(listaNomes)

    if opcao == 6:
        biblioLista.position(listaNomes)