print("Informe quantos valores quiser, quando quiser parar, digite '-1'")
n = 0
i = 0
soma = 0
while n != -1:
    n = int(input("Informe um valor\n"))
    if n == -1:
        break
    soma += n
    i += 1
media = soma / i
print("A média é de: %.2f"%(media))
