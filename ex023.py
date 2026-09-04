n = input("Digite um número de 0 a 9999: ")

n = list(n)

def mudar():
    if len(n) <= 3:
        contador = 0
        n.insert(contador, "não possui")
        contador = contador + 1
        mudar()
    elif len(n) >= 5:
        print("Caracter maior/menor que o esperado.")

mudar()

print(f"Unidade: {n[3]}, Dezena: {n[2]}, Centena: {n[1]}, Milhar: {n[0]}")
