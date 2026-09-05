nome = input("Digite seu nome completo: ")

nome = nome.split()

quantidade = len(nome)

print(f"primeiro nome: {nome[0]}")
print(f"Último nome: {nome[quantidade - 1]}")
