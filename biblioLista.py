def insert(listaNomes):
    while True:
        try:
            insere = input('\nDigite o nome que deseja inserir: ')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break
    while True:
        try:
            listaNomes.append(insere)
            print('\nInserido com sucesso!\n')
            break
        except:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return listaNomes

def insertEspecific(listaNomes):
    while True:
        try:
            posicao = int(input('\nDigite a posicao que deseja inserir: '))
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break
    while True:
        try:
            insere = input('\nDigite o nome que deseja inserir: ')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break
    while True:
        try:
            listaNomes.insert(posicao, insere)
            print('\nInserido com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return listaNomes

def alter(listaNomes):
    while True:
        try:
            altera = input('\nDigite o nome que deseja alterar: ')
            posicao = listaNomes.index(altera)
            listaNomes.remove(altera)
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    while True:
        try:
            novoNome = input('\nDigite o novo nome: ')
            listaNomes.insert(posicao, novoNome)
            print('\nInserido com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return listaNomes

def delete(listaNomes):
    while True:
        try:
            listaNomes.pop()
            print('\nUltimo valor deletado com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return listaNomes

def deleteEspecific(listaNomes):
    while True:
        try:
            remove = input('\nDigite o nome que quer excluir: ')
            listaNomes.remove(remove)
            print('\nDeletado com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return listaNomes

def position(listaNomes):
    while True:
        try:
            posicao = input('\nDigite o nome a ser analisado: ')
            print('\nO nome',posicao,'esta na posicao',listaNomes.index(posicao),'!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break