numPedidos = int(input())
pedidos = []
for numero_pedido in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    vegano = input().lower()
    if vegano == "s":
      pedido = f"Pedido {numero_pedido}: {prato} (Vegano) - {calorias} calorias"
    else:
      pedido = f"Pedido {numero_pedido}: {prato} (Nao-vegano) - {calorias} calorias"
    pedidos.append(pedido)

for pedido in pedidos:
   print(pedido)
