import os

restaurantes = []

def finalizar_app():
    
    exibir_titulo('Finalizando o app ^.^')


def exibir_nome_programa():
    
    print('\x1b[6;30;42m' + '''
    ╔╝╝╝╗──╔╗───────╔╝╝╝╗
    ║╔╝╗║──║║───────║╔╝╝╝
    ║╚╝╝╦╝╝╣╚╝╦╝╝╦╝╗║╚╝╝╦╗╔╦╝╝╦╝╦╝╝╦╝╝╦╝╝╗
    ╚╝╝╗║╔╗║╔╗║╔╗║╔╝║╔╝╝╩╬╬╣╔╗║╔╣║╝╣╝╝╣╝╝╣
    ║╚╝╝║╔╗║╚╝║╚╝║║─║╚╝╝╦╬╬╣╚╝║║║║╝╬╝╝╠╝╝║
    ╚╝╝╝╩╝╚╩╝╝╩╝╝╩╝─╚╝╝╝╩╝╚╣╔╝╩╝╚╝╝╩╝╝╩╝╝╝
    ───────────────────────║║
    ───────────────────────╚╝\n'''+ '\x1b[0m')


def exibir_opcoes():

    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Alternar status do restaurante')
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
    categoria_restaurante = input('\nDigte a categoria: ')    
    
    restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status': False}
    
    restaurantes.append(restaurante)
    
    print(f'\n\x1b[6;30;42m✔ O restaurante "{nome_restaurante}" foi adicionado com sucesso!\x1b[0m')
    
    voltar_ao_menu()
    

def listar_restaurantes():
    
    exibir_titulo('Listar restaurantes')
    
    if len(restaurantes) > 0:
    
        print(f'{'Nome restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    
        for restaurante in restaurantes:
            
            status = 'Ativado' if restaurante['status'] else 'Desativado'
             
            print(f'> {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {status}')
    
    else:
        print('Lista vazia!')
        
    voltar_ao_menu()
    

def alternar_status_restaurante():
    
    exibir_titulo('Listar restaurantes')
    
    nome_restaurante = input('Digite nome do restaurante:')
    
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        
        if nome_restaurante == restaurante['nome']:
            
            restaurante_encontrado = True
            
            restaurante['status'] = not restaurante['status']            
            
            mensagem = f'Restaurante {restaurante['nome']} ativo!' if restaurante['status'] == True else f'Restaurante {restaurante['nome']} desativado!'
    
            print(mensagem)
    
    if not restaurante_encontrado:
        
        print(f'\nRestaurante {nome_restaurante} não foi encontrado!')    
    
    voltar_ao_menu()



def escolher_opcao():
  
    try:

        opcao_escolhida = int(input('Escolha uma opção: ').strip())
      
        if opcao_escolhida == 1:
            
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            
            listar_restaurantes()

        elif opcao_escolhida == 3:
            
            alternar_status_restaurante()
            
        elif opcao_escolhida == 4:
            
            finalizar_app()
            
        else:
            
            opcao_invalida()
            
    except Exception as e:
        
        print(e)
        
        #opcao_invalida()

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


