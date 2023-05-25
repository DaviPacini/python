n = int(input("Informe a quantidade de notas: \n"))

nota = 0
for w in range(0, n, +1):
    z = float(input("Informe a nota:\n"))
    nota += z
#a partir daqui não está no for
media = nota / n
print("A média do aluno foi: %.2f"%(media))
print("*"*20)
#considerando a média do colégio como 5...
if media >= 5:
    print("Aluno APROVADO")
else:
    print('Aluno REPROVADO')
