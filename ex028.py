import random

num = random.randint(0, 5)

tentativa = int(input ("Digite qual numero você acha que eu escolhi (entre 0 e 5): "))
if tentativa == num:
    print("Você venceu!")
    print(f"o número era {num}")

else:
    print("Você peredeu!")
    print(f"o número era {num}")