def main():
    print('\nInsira 3 números menores que 16')
    num1 = int(input('Número 1: '))
    num1_binario = binario(num1)
    num2 = int(input('Número 2: '))
    num2_binario = binario(num2)
    num3 = int(input('Número 3: '))
    num3_binario = binario(num3)
    
    soma_nim(num1_binario, num2_binario, num3_binario)

def binario(num):
    num_base10 = num
    pot0 = num % 2
    num = num // 2
    pot1 = num % 2
    num = num // 2
    pot2 = num % 2
    num = num // 2
    pot3 = num % 2
    
    num_binario = str(pot3) + str(pot2) + str(pot1) + str(pot0)
    
    print(f'O número {num_base10} em código binário é {num_binario}\n')

    return num_binario

def soma_nim(num1, num2, num3):
    pot3 = ((int(num1[0]) + int(num2[0]) + int(num3[0])) % 2)
    pot2 = ((int(num1[1]) + int(num2[1]) + int(num3[1])) % 2)
    pot1 = ((int(num1[2]) + int(num2[2]) + int(num3[2])) % 2)
    pot0 = ((int(num1[3]) + int(num2[3]) + int(num3[3])) % 2)
    
    soma_nim = str(pot3) + str(pot2) + str(pot1) + str(pot0)
    
    print(f'\nA soma-nim dos três números é {soma_nim}')
    
main()
