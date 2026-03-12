import random

def gerar_numeros():
    lista = []
    for i in range(5):
        num = random.randint(1, 10)
        lista.append(num)
    return lista

def contar_acertos(sorteados, jogador):
    acertos = 0
    for n in jogador:
        if n in sorteados:
            acertos = acertos + 1
    return acertos


numeros_usuario = []

print("Digite 5 números para comparar com os números gerados")

for i in range(5):
    valor = int(input("Digite um número: "))
    numeros_usuario.append(valor)

numeros_sorteados = gerar_numeros()

print("Números gerados pela máquina =", numeros_sorteados)
print("Números escolhidos pelo usuário =", numeros_usuario)

resultado = contar_acertos(numeros_sorteados, numeros_usuario)

print("Quantidade de números acertados =", resultado)