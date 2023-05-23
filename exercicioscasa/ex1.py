salario = float(input("Informe o valor do salário bruto: \n"))
fgts = salario * 0.08
salarioliq = salario - fgts
print("Salário líquido: %.f"%(salarioliq))
print("FGTS: %.f"%(fgts))