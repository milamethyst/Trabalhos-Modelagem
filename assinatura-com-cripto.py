def le_arquivo():
    arquivo = open('Hash.txt', 'r')
    mensagem = arquivo.readline().strip()
    arquivo.close()
    return mensagem

def cria_lista_assinatura():
    lista = []
    arquivo = open('TesteAssinatura.txt', 'r', encoding='utf-8')
    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close()
    return lista

def hexadecimal(num):
    hexa = ''
    while num != 0:
        resto = num % 16
        if resto > 9:
            if resto == 10:
                hexa += 'a'
            elif resto == 11:
                hexa += 'b'
            elif resto == 12:
                hexa += 'c'
            elif resto == 13:
                hexa += 'd'
            elif resto == 14:
                hexa += 'e'
            elif resto == 15:
                hexa += 'f'
        else:
            hexa += str(resto)
        num //= 16
    return hexa

def criar_hash(string):
    hash = ''
    for char in string:
        hash += str(ord(char))
    hash = int(hash) % 16 ** 50
    hash = hexadecimal(hash)
    return hash

def cria_lista_hash(lista):
    lista_hash = []
    for elem in lista:
        hash = criar_hash(elem)
        lista_hash.append(hash)
    return lista_hash

def testa_assinatura(string, lista):
    for i, elem in enumerate(lista):
        if elem == string:
            print(f'Índice: {i}')
            return i
    
def exibir_mensagem(i, lista):
    print(f'O conteúdo do arquivo assinado digitalmente é: {lista[i]}')

hash_original = le_arquivo()
lista_padrao = cria_lista_assinatura()
lista_hash = cria_lista_hash(lista_padrao)
i = testa_assinatura(hash_original, lista_hash)
exibir_mensagem(i, lista_padrao)