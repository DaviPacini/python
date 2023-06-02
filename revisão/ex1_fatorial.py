n = int(input("Informe um valor\n"))
resultado=1
if n == 0:
    print(resultado)
else:
    for z in range(1, n+1):
        resultado *= z
        print(resultado)