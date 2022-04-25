try:
    peso = 54
    altura = 1.56
    imc = peso/(altura*altura)
    print("imc = ", imc)

    if 0 < imc <= 18.5:
        print("Magreza")
    elif 18.5 < imc <= 24.9:
        print("Normal")
    elif 24.9 < imc <= 30:
        print ("Sobrepeso")
    elif 30 < imc:
        print("Obesidade")
    else:
        print("ERRO:  peso: ", peso, "altura: ", altura)

except Exception as e:
    print("ERRO: ", str(e))


