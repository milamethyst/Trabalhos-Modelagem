def sequencia_nova(sequencia, n):
    seq_nova = []
    for i in range(1, len(sequencia) + 1):
        if i == 1 or i % n != 0:
            seq_nova.append(sequencia[i - 1])
    
    print(f'Sequência restante: {seq_nova}\n')
    somas = [1]
    
    for i in range(1, len(seq_nova) - 1):
        somas.append(seq_nova[i] + somas[i - 1])
    
    print(f'Somas parciais: {somas}\n')
    
    if n > 2:
        somas = sequencia_nova(somas, n - 1)
    
    return somas

def sequencia_inicial(n):
    sequencia = list(range(1, 10 * n + n))
    return sequencia

n = int(input('Insira um número natural n: '))
sequencia = sequencia_inicial(n)
print(f'Sequência inicial: {sequencia}\n')

soma_final = sequencia_nova(sequencia, n)

print(f'\nPrimeiras 10 potências do expoente {n}')

for i, elem in enumerate(soma_final):
    print(f'{i + 1}^{n} = {elem}')
