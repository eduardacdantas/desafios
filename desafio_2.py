def calcular_preco():
  valorHamburguer = float(input())
  quantidadeHamburguer = int(input())
  valorBebida = float(input())
  quantidadeBebida = int(input())
  valorPago = float(input())
  valor_total_hamburguer = valorHamburguer * quantidadeHamburguer
  valor_total_bebida = valorBebida * quantidadeBebida
  preco_total_pedido = valor_total_bebida + valor_total_hamburguer
  troco_final = valorPago - preco_total_pedido
  print(f"O preço final do pedido é R$ {preco_total_pedido:.2f}. Seu troco é R$ {troco_final:.2f}.")
calcular_preco()
