num = int(input("Digite a distância em Km: "))

if num <= 200:
    valor = num * 0.50
    print(f"Sua viagem vai custar R$: {valor}")

else:
    valor = num * 0.45
    print(f"Sua viagem vai custar R$: {valor}")