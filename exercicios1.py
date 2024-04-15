#Imprima a frase: Python na Escola de Programação da Alura.

print('Python na Escola de Progrmação XYZ')


#Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = 'Marcelo'
idade = '36'

print(f'Meu nome é {nome} e tenho {idade} anos')


#Imprima a palavra: 'ALURA' de modo que cada letra fique em uma linha, como mostrado a seguir:

palavra = 'ALURA'

for posicao in range(len(palavra)):
    print(palavra[posicao])
    

#Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('\nDigite um número '))

if numero % 2 == 0:
    print(f'\nO número {numero} é par')

else:
    print(f'\nO número {numero} é impar')


#Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade = int(input('Informe a sua idade '))

if idade >= 0 and idade <=12:
    
    print('\nCriança')
    
elif idade >= 13 and idade <= 18:
    
    print('\nAdolescente')
    
else:
    
    print('\nAdulto')


#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario = input('\nDigite seu usuário: ')

senha = input('\nDigite sua senha: ')

if usuario == 'marcelo' and senha == '123456':
    
    print('\nAcesso permitido!')
    
else:
    
    print('\nAcesso negado! Tente novamente.')


#Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

x = int(input('\nDigite valor de x: '))

y = int(input('\nDigite valor de y: '))

if x > 0 and y > 0:
    
    print('\nPrimeiro Quad.')
    
elif x < 0 and y >0:
    
    print('\nSegundo Quad.')
    
elif x < 0 and y < 0:
    
    print('Terceiro Quad.')
    
else:
    
    print('\nQuarto Quad.')