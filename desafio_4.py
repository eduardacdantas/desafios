def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
        #print(f"Valor total: {total:.2f}")
        
    desconto = input("")
    if desconto == "10%":
        valor_total1 = total - (total * 0.1)
        print(f"Valor total: {valor_total1:.2f}")
    elif desconto == "20%":
        valor_total2 = total - (total * 0.2)
        print(f"Valor total: {valor_total2:.2f}")
    else:
        print("Desconto escolhido inválido, por favor tente novamente!")
    

if __name__ == "__main__":
    main()
