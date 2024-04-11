import os

restaurantes = []

def finalizar_app():
    
    os.system('cls')
    
    print('Finalizando o app ^.^\n')


def exibir_nome_programa():
    
    print('\x1b[6;30;42m' + '''
    ╔═══╗──╔╗───────╔═══╗
    ║╔═╗║──║║───────║╔══╝
    ║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
    ╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
    ║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
    ╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
    ───────────────────────║║
    ───────────────────────╚╝\n'''+ '\x1b[0m')


def exibir_opcoes():

    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')


def cadastrar_novo_restaurante():
    
    os.system('cls')
    
    print('Cadastro de novos restaurantes')

    nome_restaurante = input('Deigite o nome do restaurante: ')
    
    restaurantes.append(nome_restaurante)
    
    print(f'\nO restaurante {nome_restaurante} foi adicionado com sucesso!\n ')
    
    input('Digite uma tecla para voltar ao menu ')
    
    main()

def escolher_opcao():

    try:

        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            
            print('Listar restaurantes')

        elif opcao_escolhida == 3:
            
            print('Ativar restaurante')
            
        elif opcao_escolhida == 4:
            
            finalizar_app()
            
        else:
            
            opcao_invalida()
            
    except:
        
        opcao_invalida()

def opcao_invalida():
    
    print('Opção inválida!\n')
    input('Digite uma tecla pra voltar ao menu principal ')
    main()

def main():
    
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

#tornando o script como principal; não poderá ser importado por outros scripts
if __name__ == '__main__':
    main()

#print(f'\nVocê escolheu a opção: {opcao_escolhida}')
#print(type(opcao_escolhida))

#exemplo formatação float
#print(f'O valor arredondado de pi é: {pi:.2f}')


