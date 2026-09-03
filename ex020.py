import random
al1 = input("Aluno 1")
al2 = input("Aluno 2")
al3 = input("Aluno 3")
al4 = input("Aluno 4")

ordem = random.sample((al1, al2, al3, al4), k=4)

print(f"A ordem de apresentação vai ser: {ordem}")