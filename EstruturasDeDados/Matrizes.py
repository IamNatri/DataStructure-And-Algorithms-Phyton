import numpy as np

matriz = np.array([[2, 3 ,1], [4, 5, 7]])

print(matriz)
print("========shape========")

print(matriz.shape)
print("=========sum=======")
print(matriz.sum())
print("==========matriz[0]======")
print(matriz[0])
print("=====matriz[1]===========")
print(matriz[1])
print("======matriz[0][2]==========")
print(matriz[0][2])
print("========LACO PERCORRENDO A MATRIZ ========")

print("Formato da matriz", matriz.shape)
for i in range(matriz.shape[0]):
    print(matriz[i])
for i in range(matriz.shape[0]):#percorrendo as linhas
    for j in range(matriz.shape[1]):#percorrendo colunas
        print(matriz[i][j])
