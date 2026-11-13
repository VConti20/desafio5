qtd_vendas=0
valor_total=0

while True:
    valor_de_venda=float(input("Valor de venda (aperte 0 para encerrar): R$ "))
    if valor_de_venda <= 0:
        break
    valor_total+=valor_de_venda
    qtd_vendas+=1

print(f"Vendas registradas: {valor_total:.2f}")
print(f"Total de venda: {qtd_vendas}")