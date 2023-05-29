print("Informe quantos valores quiser, quando quiser parar, digite '-1'")
n = 0
i = 0
soma = 0
while n != -1:
    n = int(input("Informe um valor\n"))
    soma += n
    if n == -1:
        soma += 1
        i -= 1
    i += 1
media = soma / i
print("A média é de: %.2f"%(media))
