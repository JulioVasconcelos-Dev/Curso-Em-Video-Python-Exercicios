def minha_tentativa():
    nome = input ("Digite o nome da sua cidade: ")

    nome = nome.title()
    nome = nome.split()

    if "Santo" in nome[0]:
        print('Sua cidade começa com "Santo".')

    else:
        print('Sua cidade não começa com "Santo"')

def curso():
    nome = str(input("Digite o nome de sua cidade: "))
    print(nome[:5] == "Santo")