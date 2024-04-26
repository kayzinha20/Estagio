def calculoImc():
    peso= float(input("Informe o peso:"))
    altura=float(input("Informe a altura:"))
    imc=peso/altura*2
    print(imc)
    return
calculoImc()