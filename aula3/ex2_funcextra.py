def div(a):
    z = a % 2
    if z == 0:
        print("%d é múltiplo de 2"%(a))
    else:
        print("%d NÃO é múltiplo de 2"%(a))


w = int(input("Informe um valor:\n"))
div(w)


