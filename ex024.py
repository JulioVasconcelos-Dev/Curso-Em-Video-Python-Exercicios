nome = input ("Digite o nome da sua cidade: ")

nome = nome.title()
nome = nome.split()

if "Santo" in nome[0]:
    print('Sua cidade começa com "Santo".')

else:
    print('Sua cidade não começa com "Santo"')