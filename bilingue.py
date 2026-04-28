def main():
    print('=== IDENTIFICADOR DE NÚMEROS BILÍNGUES ===') 
    b = int(input('Insira uma base b (1<b<10): '))
    n = input(f'Insira um número inteiro escrito na base {b}: ')
    n = muda_decimal(n, b)
    
    contador = 2
    bilingue = False
    
    print(f'\n== Número {n} ==') # print do número em todas as bases
    for i in range(2, 10):
        print(f'Na base {i}: {muda_base(n, i)}')
        
    while contador < 10:
        contador_compara = contador + 1
        while contador_compara < 10:
            igual = True
            n1 = muda_base(n, contador)
            n2 = muda_base(n, contador_compara)
            for i in range(len(n1)):
                if n1[i] not in n2: # se qualquer algarismo não for igual, altera o bool "igual" para False
                    igual = False
            for i in range(len(n2)):
                if n2[i] not in n1: # se qualquer algarismo não for igual, altera o bool "igual" para False
                    igual = False
            if igual: # se não foi encontrado nenhum algarismo diferente, então o número é bilíngue naquelas duas bases
                if bilingue == False:
                    print('\nEste número é bilíngue nas seguintes bases:') # esse print ocorre apenas na primeira vez em que se descobre que o número é bilíngue
                    bilingue = True
                print(f'- {contador} e {contador_compara}') # exibe a base e o número naquela base entre parênteses
            contador_compara += 1
        contador += 1
        
    if bilingue == False:
        print('\nEste número não é bilíngue')

def muda_base(n, b):
    num_base_b = 0
    contador = 0
    while n > 0:
        resto = n % b
        n = n // b
        num_base_b += resto * 10 ** contador
        contador += 1
    return str(num_base_b) 
    
def muda_decimal(num_base_b, b):
    num_base_decimal = 0
    for i in range(len(num_base_b)):
        n = int(num_base_b[i])
        num_base_decimal += n * b ** (len(num_base_b) - i - 1)
    return num_base_decimal

main()
