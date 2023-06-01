"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

A) Faça uma tabuada usando FOR dentro de um WHILE.
B) Faça um código, usando for , que mostre todas as tabuadas(1 até 10)."""

def tabuada(a):
    print(
        a, "x 1 = ", a*1, "\n",
        a, "x 2 = ", a * 2, "\n",
        a, "x 3 = ", a * 3, "\n",
        a, "x 4 = ", a * 4, "\n",
        a, "x 5 = ", a * 5, "\n",
        a, "x 6 = ", a * 6, "\n",
        a, "x 7 = ", a * 7, "\n",
        a, "x 8 = ", a * 8, "\n",
        a, "x 9 = ", a * 9, "\n",
        a, "x 10 = ", a * 10, "\n",
    )
n = int(input("Informe o número desejado:\n"))
tabuada(n)
#a\b) ==================
i = 0
while i != 10:
    for i in range(0, 11):
        print(
            i, "x 1 = ", i * 1, "\n",
            i, "x 2 = ", i * 2, "\n",
            i, "x 3 = ", i * 3, "\n",
            i, "x 4 = ", i * 4, "\n",
            i, "x 5 = ", i * 5, "\n",
            i, "x 6 = ", i * 6, "\n",
            i, "x 7 = ", i * 7, "\n",
            i, "x 8 = ", i * 8, "\n",
            i, "x 9 = ", i * 9, "\n",
            i, "x 10 = ", i * 10, "\n",
        )
        i += 1
    break


