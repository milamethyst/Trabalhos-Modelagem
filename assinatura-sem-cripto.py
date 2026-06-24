def le_arquivo():
    arquivo = open('Documento.txt', 'r', encoding='utf-8')
    mensagem = arquivo.readline().strip()
    arquivo.close()
    return mensagem

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

def salva_arquivo(string):
    arquivo = open('Hash.txt', 'w')
    arquivo.write(string)
    arquivo.close()

mensagem = le_arquivo()
mensagem = criar_hash(mensagem)
salva_arquivo(mensagem)

