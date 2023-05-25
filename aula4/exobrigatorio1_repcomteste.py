n = int(input("Informe a quantidade de números a serem informados:\n"))
z = 0
i = 0
lista = []
for w in range(0, n, +1):
    num = int(input("Informe um número\n"))
    lista.insert(z, num)
    z += 1
for i in range(len(lista)):
    if lista[i] > 0:
        print(lista[i])
    else:
        print("1")
    i += 1

