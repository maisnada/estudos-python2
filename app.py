import os

def finalizar_app():
    
    os.system('cls')
    
    print('Finalizando o app ^.^💀\n')

print('\x1b[6;30;42m' + '''
╔═══╗──╔╗───────╔═══╗
║╔═╗║──║║───────║╔══╝
║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
───────────────────────║║
───────────────────────╚╝\n'''+ '\x1b[0m')

print('1 - Cadastrar restaurante')
print('2 - Listar restaurante')
print('1 - Ativar restaurante')
print('1 - Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

if opcao_escolhida == 1:
    
    print('Cadastrar restaurante')
    
elif opcao_escolhida == 2:
    
    print('Listar restaurantes')

elif opcao_escolhida == 3:
    
    print('Ativar restaurante')
    
else:
    
    finalizar_app()

#print(f'\nVocê escolheu a opção: {opcao_escolhida}')
#print(type(opcao_escolhida))

#exemplo formatação float
#print(f'O valor arredondado de pi é: {pi:.2f}')


