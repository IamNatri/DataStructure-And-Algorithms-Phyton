
print("Digite sua idade: ")
idade = int(input())

if (idade < 0):
    print('idade invalida!')
elif (idade <= 12):
    print("Criança")
elif(idade >= 13 or idade <= 18):
    print("adolescente")
else:
    print("Adulto")


#=============================#

print("Digite sua primeira nota: ")
m1 = int(input())
print("Digite sua segunda nota: ")
m2 = int(input())
print("Digite sua terceira nota: ")
m3 = int(input())
media = (m1+m2+m3)/3
print(media)

if(media >= 0 and media <= 4):
    print("Reprovado")
elif (media >= 4.1 and media < 6):
    print("Pegou exame")
    print("Informe nota do exame: ")
    notaExame = int(input())
    if(notaExame >= 6):
        print("Aprovadp!")
    else:
        print("Reprovado!")
else:
    print("Aprovado!")


