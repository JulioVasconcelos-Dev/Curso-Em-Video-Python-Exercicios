import random
import os
os.system("cls")
al1 = input("Digite o nome do aluno 1: ")
al2 = input("Digite o nome do aluno 2: ")
al3 = input("Digite o nome do aluno 3: ")
al4 = input("Digite o nome do aluno 4: ")

aluno_sorteado = random.choice((al1, al2, al3, al4))

print(f"O aluno sorteado é {aluno_sorteado}")