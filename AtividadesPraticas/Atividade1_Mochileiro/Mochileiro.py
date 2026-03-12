limiteMochila = 23
pesoAtual = 0
listaItens = []

nomeMochileiro = input("\nDigite o nome do mochileiro: ")

entrada = ""

while entrada != "fim":
    entrada = input("\nDigite o nome do item ou 'fim' para encerrar: ")

    if entrada != "fim":
        pesoItem = float(input("\nDigite o peso do item (kg): "))

        if pesoAtual + pesoItem > limiteMochila:
            print("Peso excede o limite da mochila. Item não adicionado.")
            if len(listaItens) > 0:
                break
        else:
            listaItens.append((entrada, pesoItem))
            pesoAtual = pesoAtual + pesoItem
            print("Item adicionado com sucesso!")

espacoLivre = limiteMochila - pesoAtual

print("\nMochileiro:", nomeMochileiro)
print("Peso total:", f"{pesoAtual:.2f}Kg")
print("Espaço restante:", f"{espacoLivre:.2f}Kg")

if len(listaItens) == 0:
    print("Mochila está vazia")
else:
    print("Itens adicionados:")
    for nomeItem, pesoItem in listaItens:
        print("-", nomeItem + ":", f"{pesoItem:.2f}Kg")