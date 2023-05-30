i = 0
par = 0
soma = 0
lista = []
while True:
    n = int(input("Informe um valor inteiro: \n"))
    i += 1 #quantidade de números
    soma += n #soma dos números
    media = soma / i
    npar = n % 2 #teste para saber se é par
    if npar == 0:
        par += 1
    porcpar = (par / i)*100 #porcentagem de números pares
    lista.append(n)

    print("\t*"+"Quantidade de elementos:  %d"%(i) )
    print("\t*"+"Soma dos valores:  %d"%(soma))
    print("\t*"+"Média dos valores:  %.2f"%(media))
    print("\t*"+"Total de pares:  %.2f"%(porcpar)+"%")
    print("\t*"+"Valores:  ",lista)
