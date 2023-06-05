valores = []
soma = 0
i = 0
n = 0
quant_par = 0
print('Para parar o Loop, digite -1')

while True:
    n = int(input("Informe o valor: \n"))
    if n != -1:
        valores.append(n)
    else:
        break
    par = n % 2
    if par == 0:
        quant_par += 1

#calculando a média:
for i in range(len(valores)):
    soma += valores[i]
    i += 1
media = soma / i

#porcentagem de pares
porcentagem = (quant_par / len(valores))*100

print("\t"+'*'*40)
print('\t*'+f"Número de elementos: {len(valores)}")
print('\t*'+f'Soma dos valores: {sum(valores)}')
print('\t*'+f'A média é: {media}')
print('\t*'+f'A porcentagem é de: {porcentagem}')
print("\t"+'*'*40)