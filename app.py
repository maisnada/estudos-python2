import os

restaurantes = []

def finalizar_app():
    
    exibir_titulo('Finalizando o app ^.^')


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

def exibir_titulo(titulo):
    
    os.system('cls')
    
    print(f'▷ {titulo}\n')
    
    
def voltar_ao_menu():
    
    input('\nDigite uma tecla para voltar ao menu ')
    
    main()


def cadastrar_novo_restaurante():
    
    exibir_titulo('Cadastrar novo restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante: ')
    
    restaurantes.append(nome_restaurante)
    
    print(f'\n\x1b[6;30;42m✔ O restaurante "{nome_restaurante}" foi adicionado com sucesso!\x1b[0m')
    
    voltar_ao_menu()
    

def listar_restaurantes():
    
    exibir_titulo('Listar restaurantes')
    
    for restaurante in restaurantes:
        
        print(f'☉ {restaurante}')
    
    voltar_ao_menu()
    

def escolher_opcao():

    try:

        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            
            listar_restaurantes()

        elif opcao_escolhida == 3:
            
            print('Ativar restaurante')
            
        elif opcao_escolhida == 4:
            
            finalizar_app()
            
        else:
            
            opcao_invalida()
            
    except:
        
        opcao_invalida()

def opcao_invalida():
    
    os.system('cls')
    
    print('\x1b[5;30;41m✘ Opção inválida!\x1b[0m\n')
    
    voltar_ao_menu()

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


