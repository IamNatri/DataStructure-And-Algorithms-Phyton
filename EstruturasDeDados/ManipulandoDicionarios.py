notasAlunos = {}

for i in range(3):
    nome = input(f"Insira o nome do aluno {i}: ")
    nota = int(input(f"Insira o nota do aluno {i}: "))
    notasAlunos[nome] = nota
soma = 0
for nome, nota in notasAlunos.items():
    soma = nota + soma

media = soma / 3 
print(media)