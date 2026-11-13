senha = "python"

for tentativa in range(3):
    tenta = input("Digite a senha: ")

    if tenta == senha:
        print("Acesso liberado!")
        break
    else:
        restantes = 2 - tentativa
        if restantes > 0:
            print(f"Senha incorreta. Você tem mais {restantes} tentativa(s).")
else:
    print("Você errou a senha 3 vezes...")
    print("Acesso bloqueado")
