qtd_aluno=int(input("Quantos alunos na turma? "))
nota_total=0
contador=1
for nota in range(qtd_aluno):
    nota_do_aluno=float(input(f"Nota do aluno {contador} : "))
    contador+=1
    nota_total+=nota_do_aluno

print(f"Média da turma: {nota_total/qtd_aluno:.1f}")

