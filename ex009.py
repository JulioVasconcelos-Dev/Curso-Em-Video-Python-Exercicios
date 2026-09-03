n = int(input("Digite um número: "))
m = 1
contador = 1
while True:
    print(f"{n} x {m} = {n * m}")
    m = m + 1
    contador = contador + 1
    if contador == 11:
        break
