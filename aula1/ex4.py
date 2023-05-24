altura = float(input("Informe a altura: \n"))
peso = float(input("Informe o peso: \n"))
imc = peso/(altura*altura)
if imc < 18.5:
    print("Você está abaixo do peso ideal, com o imc de: %.2f"%(imc))
elif imc >= 18.5 and imc < 25.0:
    print("Você está no peso ideal, com ic de: %.2f"%(imc))
elif imc >= 25 and imc < 30 :
    print("Você está com sobrepeso, com imc de: %.2f"%(imc))
elif imc >= 30:
    print("Você está com obesidade, com imc de: %.2f"%(imc))


