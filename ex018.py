import math
num = int(input("Digite um ângulo: "))

seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))

print(f"Seno de {num} é {seno:.2f}\nCosseno de {num} é {cosseno:.2f}\nTangente de {num} é {tangente:.2f}")