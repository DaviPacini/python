#Definição das variáveis
notas = []
#Como parar o Loop
print("\nPara parar de inserir valores, digite '-1'\n")
#Loop
while True:
    n = float(input('Informe a nota:\n'))
    #Condição de parada
    if n == -1:
        break
    notas.append(n)
#Definição da média da turma
media = sum(notas) / len(notas)
#Apresentação no prompt
print('\t'+'*'*40)
print('\t*'+f'As notas foram: {notas}')
print('\t*'+f'A média da turma foi: {media: .2f}')
print('\t'+'*'*40)