i = 0
par = 0
soma = 0
while True:
    n = int(input("Informe um valor inteiro: \n"))
    i += 1
    soma += n
    media = soma / i
    npar = n % 2
    if npar == 0:
        par += 1
    porcpar = (par / i)*100

    print("\t*"+"Quantidade de elementos:  %d"%(i) )
    print("\t*"+"Soma dos valores:  %d"%(soma))
    print("\t*"+"Média dos valores:  %.2f"%(media))
    print("\t*"+"Total de pares:  %.2f"%(porcpar)+"%")
