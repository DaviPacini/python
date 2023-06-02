n = int(input("Quantos números da tabela você deseja ver?\n"))
i = 2
z = 1
fibonacci = [1, 1]
if n == 1 or n == 2:
    print(fibonacci[n-1])

else:

    for i in range(n-2):
        y = fibonacci[i-1] + fibonacci[i - 2]
        fibonacci.append(y)
        i += 4
    print(fibonacci)
