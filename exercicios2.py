#Crie uma lista para cada informa��o a seguir:
#Lista de n�meros de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que voc� nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nomes = ["rosa", "bruno", "vanessa", "marcelo"]

anos = [1987, 2024]

#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for nome in nomes:
    print(f'{nome}')
    
for i in range(len(nomes)):
    print(f'{nomes[i]}')

n = 0

while n < len(nomes):
    print(f'{nomes[n]}')
    n += 1

#Utilize um loop for para calcular a soma dos n�meros �mpares de 1 a 10.

soma_impares = 0

for numero in numeros:
    
    if numero % 2 != 0:
        soma_impares += numero
    
print(f'Soma dos números ímpares é {soma_impares}')

#Utilize um loop for para imprimir os n�meros de 1 a 10 em ordem decrescente.

c = len(numeros) - 1 

while c >= 0:
    print(f'#{numeros[c]}')
    c-= 1

#Solicite ao usu�rio um n�mero e, em seguida, utilize um loop for para imprimir a tabuada desse n�mero, indo de 1 a 10.

tabuada = int(input('informe a tabuada: '))

for c in range(1, 11):
    
    print(f' {tabuada} x {c} = {tabuada * c}')

#Crie uma lista de n�meros e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com poss�veis exce��es.

soma = 0

numeros.append("teste")

try:
    for numero in numeros:
        
        soma += numero
        
    print(f'Soma é {soma}')

except Exception as e:
    print(f'Ocorreu erro: {e}')

#Construa um c�digo que calcule a m�dia dos valores em uma lista. Utilize um bloco try-except para lidar com a divis�o por zero, caso a lista esteja vazia.

numeros.clear()

soma_num = 0

try:
    for numero in numeros:
        
        soma_num += numero
        
    print(f'Soma é {soma_num}')

except Exception as e:
    print(f'Ocorreu erro: {e}')

