pares = []
impares = []
positivos = []
negativos = []

i = 0
while i < 5:
    n = int(input("Informe um valor\n"))
    if n >= 0:
        positivos.append(n)
    else:
        negativos.append(n)
    verificador = n % 2
    if verificador == 0:
        pares.append(n)
    else:
        impares.append(n)
    i += 1

print('\t'+'*'*40)
print('\t*\t'+f'{len(pares)} valor(es) par(es)')
print('\t*\t'+f'{len(impares)} valor(es) ímpar(es)')
print('\t*\t'+f'{len(positivos)} valor(es) positivo(s)')
print('\t*\t'+f'{len(negativos)} valor(es) negativo(s)')
print('\t'+'*'*40)
