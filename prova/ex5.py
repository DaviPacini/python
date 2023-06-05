salario = int(input("Informe o salário: \n"))
if salario > 0:
    if salario >= 1200:
        print('Dentro da Legislação')
    else:
        print('Fora da lesgislação')
else:
    print('Salário Invalido')

