contador=0
for numero in range(1, 51):
    if numero % 2 == 0:
        print(numero)
        contador += 1

print(f"Total de pares  : {contador}")