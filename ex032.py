#um ano bissexto é divisível por 4 exceto terminados em 00
#se terminar em 00 tem que ser divisivel por 400
ano = int(input("Digite um ano: "))

if ano % 100 >= 1:
    if ano % 4 >= 1:
        print(f"{ano} não é bissexto")
    else:
        print(f"{ano} é bissexto")

else:    
    if ano % 400 >= 1:
        print(f"{ano} não é bissexto")
    else:
        print(f"{ano} é bissexto")