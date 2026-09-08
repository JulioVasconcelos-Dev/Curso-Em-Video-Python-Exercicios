nome_completo = input("Digite seu nome completo: ")

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo.replace(" ", "")))
print(f"Seu primeiro nome é {nome_completo.split()[0]} e ele tem {len(nome_completo.split()[0])} letras")
