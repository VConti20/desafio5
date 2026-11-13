premiado=0

for cliente in range(1,31):
    if cliente % 3 == 0 and cliente % 5 == 0:
        print(f"Cliente {cliente}: brinde e desconto")
    elif cliente % 3 == 0:
        print(f"Cliente {cliente}: brinde")
    elif cliente % 5 == 0:
        print(f"Cliente {cliente}: desconto")
    else:
        continue
    premiado+=1
print(f"Clientes premiados: {premiado}")
