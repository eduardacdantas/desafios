def mensagem_tempo():
	nomeRestaurante = input()
	tempo_entrega = int(input())
	mensagem = f"O restaurante {nomeRestaurante} entrega em {tempo_entrega} minutos"
	print(mensagem)

	return mensagem

mensagem_tempo()
