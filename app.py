import os

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
    print('1 - Ativar restaurante')
    print('1 - Sair\n')

def escolher_opcao():

    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        
        print('Cadastrar restaurante')
        
    elif opcao_escolhida == 2:
        
        print('Listar restaurantes')

    elif opcao_escolhida == 3:
        
        print('Ativar restaurante')
        
    else:
        
        finalizar_app()


def main():
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


