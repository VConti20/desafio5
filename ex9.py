qtd_de_venda = int(input("Quantas vendas foram feitas: "))

if qtd_de_venda > 0:
  total_de_vendas = 0
  maior_valor = 0
  menor_valor = 0

  for venda in range(qtd_de_venda):
    valor = float(input("Digite o valor do produto: R$ "))
    total_de_vendas += valor

    if venda == 0:
      maior_valor = valor
      menor_valor = valor
    else:
      if valor > maior_valor:
        maior_valor = valor
      if valor < menor_valor:
        menor_valor = valor

  media = total_de_vendas / qtd_de_venda

  print(f"Menor valor: R$ {menor_valor:.2f}")
  print(f"Maior valor: R$ {maior_valor:.2f}")
  print(f"Média: R$ {media:.2f}")
else:
  print("Nenhuma venda foi registrada.")
