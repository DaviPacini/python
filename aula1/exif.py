hora = int(input("Informe o Horário(apenas horas):\n"))

if 0 <= hora < 6:
    print("Agora são %d Horas. Boa Madrugada!"%(hora))
elif 6 <= hora < 12:
    print("Agora são %d Horas. Bom Dia!"%(hora))
elif 12 <= hora < 18:
    print("Agora são %d Horas. Boa Tarde!"%(hora))
elif 18 <= hora <= 24:
    print("Agora são %d Horas. Boa Noite!"%(hora))