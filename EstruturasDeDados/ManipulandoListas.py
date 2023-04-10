a = []
for i in range(5):
    b = int(input("Digite um valor: "))
    a.append(b)
soma = 0
for j  in range(len(a)):
    soma += a[j]
print(soma)