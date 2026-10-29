velocidade = int(input("Quantos Km/h o carro estava? "))
if velocidade >= 81:
    print("Você foi multado!")
    sub = velocidade - 80
    multa = sub * 7
    print(f"Sua multa é de R$: {multa} ")
else:
    print("Você está dentro do limite de velocidade")