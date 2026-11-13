while True:
    print("=== Academia Rio Fit ===")
    print("1 - Ver horário")
    print("2 - Calcular plano")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Segunda a sexta, das 6h às 22h.")
        print("--"*20)

    elif opcao == 2:
        meses = int(input("Quantos meses de plano? "))
        total = meses * 120

        if meses >= 6:
            total = total * 0.90

        print(f"Total do plano: R$ {total:.2f}")
        print("--"*20)

    elif opcao == 0:
        print("Até logo!")
        break

    else:
        print("Opção inválida!")
