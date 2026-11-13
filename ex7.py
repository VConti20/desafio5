senha=input("Digite uma senha: ")

numero="0123456789"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tem_numero=False
tem_maiusculo=False

for letra in senha:
    if letra in numero:
        tem_numero=True

    if letra in maiusculas:
        tem_maiusculo=True

if len(senha) >= 8 and tem_maiusculo and tem_numero:
    print("Senha Forte")
else:
    print("Senha fraca! Está faltando: ")
    if len(senha)<8:
        print("- Pelo menos 8 caractere.")
    if not tem_numero:
        print("- Pelo menos um número")
    if not tem_maiusculo:
        print("- Pelo menos uma letra maiúscula")


