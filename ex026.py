frase = input("Digite uma frase: ")

print(f'A letra "A" aparece {frase.upper().count("A")} vezes')
print(f"Aparece pela primeira vez no caractere {frase.upper().find("A")}")
print(f"Aparece pela última vez no caractere {frase.upper().rfind("A")}")