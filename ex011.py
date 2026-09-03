largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print(f"Sua área é de: {area}")
baldes = area / 2
print(f"Sabendo que cada balde de tinta cobre 2m²\n precisará de {baldes} baldes")