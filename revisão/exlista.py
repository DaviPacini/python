print("Informe os dados das empresas, digite '-1' para parar")
cnpj = 0
funcionarios = 0
func_list = []
cnpj_list = []
while cnpj != -1:
    cnpj = int(input("CNPJ:\n"))
    if cnpj == -1:
        break
    cnpj_list.append(cnpj)
    funcionarios = int(input("Funcionários: \n"))
    func_list.append(funcionarios)

cnpj_maior_empresa = cnpj_list[func_list.index(max(func_list))]
print(f"A maior empresa tem CNPJ: {cnpj_maior_empresa}, e núemero de funcionários: {max(func_list)}", )