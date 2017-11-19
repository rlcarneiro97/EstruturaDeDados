def insert(filaNomes):
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
            filaNomes.append(insere)
            print('\nInserido com sucesso!\n')
            break
        except:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return filaNomes

def insertEspecific(filaNomes):
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
            filaNomes.insert(posicao, insere)
            print('\nInserido com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return filaNomes

def alter(filaNomes):
    while True:
        try:
            altera = input('\nDigite o nome que deseja alterar: ')
            posicao = filaNomes.index(altera)
            filaNomes.remove(altera)
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    while True:
        try:
            novoNome = input('\nDigite o novo nome: ')
            filaNomes.insert(posicao, novoNome)
            print('\nInserido com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return filaNomes

def delete(filaNomes):
    while True:
        try:
            filaNomes.pop()
            print('\nUltimo valor deletado com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return filaNomes

def deleteEspecific(filaNomes):
    while True:
        try:
            remove = input('\nDigite o nome que quer excluir: ')
            filaNomes.remove(remove)
            print('\nDeletado com sucesso!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break

    return filaNomes

def position(filaNomes):
    while True:
        try:
            posicao = input('\nDigite o nome a ser analisado: ')
            print('\nO nome',posicao,'esta na posicao',filaNomes.index(posicao),'!\n')
            break
        except ValueError:
            opcao2 = int(input('\nValor inválido! Digite qualquer número para continuar ou "0" para cancelar: '))
            if opcao2 == 0:
                break