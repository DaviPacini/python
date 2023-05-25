print("Informe 10 valores")
soma = 0
for n in range(0, 10, +1):
    num = int(input("Informe um número:\n"))
    soma += num

media = soma / 10
print(media)