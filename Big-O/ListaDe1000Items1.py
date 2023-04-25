# primeira implementação de uma lista
#O(n) OR O(1000)
import timeit

startTimer = timeit.default_timer()


def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

print(lista1()) 

print("o tempo de execução é: ", timeit.default_timer() - startTimer)