def main():
    print('=== IDENTIFICADOR DE NÚMEROS BILÍNGUES ===')
    b = int(input('Insira uma base b (1<b<10): '))
    n = input(f'Insira um número inteiro escrito na base {b}: ')
    n = muda_decimal(n, b)
    contador = 2
    bilingue = False
    while contador < 10:
        contador_compara = contador + 1
        while contador_compara < 10:
            igual = True
            if contador != contador_compara:
                n1 = muda_base(n, contador)
                n2 = muda_base(n, contador_compara)
                for i in range(len(n1)):
                    if n1[i] not in n2:
                        igual = False
                for i in range(len(n2)):
                    if n2[i] not in n1:
                        igual = False
                if igual:
                    if bilingue == False:
                        print(f'O número {n} é bilíngue nas seguintes bases:')
                        bilingue = True
                        print(f'- {contador} e {contador_compara}')
                    else:
                        print(f'- {contador} e {contador_compara}')
            contador_compara += 1
        contador += 1
    if bilingue == False:
        print(f'O número {n} não é bilíngue')

def muda_base(n, b):
    final = False
    num_base_b = 0
    resto = 0
    contador = 0
    while final == False:
        resto = n % b
        n = n // b
        if n == 0:
            final = True
        num_base_b += resto * 10 ** contador
        contador += 1
    num_base_b = str(num_base_b)
    return num_base_b 
    
def muda_decimal(num_base_b, b):
    contador = 0
    num_base_decimal = 0
    while contador < (len(num_base_b)):
        n = int(num_base_b[contador])
        if n > 0:
            num_base_decimal += n * b ** (len(num_base_b) - contador - 1)
        contador += 1
    return num_base_decimal

main()
