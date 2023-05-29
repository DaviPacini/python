print("Informe no minimo 2 valores, para parar digite -1")
n = 0
valores = []
while n != -1:
    n = int(input("Informe um valor\n"))
    if n == -1: break
    valores.append(n)
print("O maior valor é: %d"%(max(valores)))
print("O menor valor é: %d"%(min(valores)))
