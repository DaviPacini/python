print("Informe quantas notas quiser. Quando desejar parar, digite '-1'")
n = 0
i = 0
soma = 0
while n != -1:
    n = float(input("Informe uma nota\n"))
    if n == -1:
        break
    soma = soma + n
    i += 1
media = soma / i
print("A média das notas foi de: %.2f"%(media))

