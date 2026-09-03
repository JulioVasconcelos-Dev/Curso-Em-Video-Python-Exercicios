dias = int(input("Quantos dias de uso? "))
km = int(input("Quantos Km percorridos? "))

valor_dia = 60 * dias
valor_km = 0.15 * km

print(f"O total a pagar é R${valor_dia + valor_km} reais")
