altura = float(input("Informe a altura: \n"))
peso = float(input("Informe o peso: \n"))
imc = peso/(altura*altura)
if imc < 18.5:
print("Você está abaixo do peso ideal, com o imc de: %.2f"%(imc))


