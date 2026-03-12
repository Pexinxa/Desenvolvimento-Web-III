def eh_primo(numero):
    if numero < 2:
        return False
    
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    
    return True


inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

contador = 0
maior_primo = None
menor_primo = None

numero = inicio

while numero <= fim:
    if eh_primo(numero):
        contador += 1
        
        if menor_primo is None:
            menor_primo = numero
        
        maior_primo = numero
    
    numero += 1


print("Quantidade de números primos:", contador)

if contador > 0:
    print("Menor primo do intervalo:", menor_primo)
    print("Maior primo do intervalo:", maior_primo)
else:
    print("Não existem números primos nesse intervalo.")