# segunda implementação de uma lista
import timeit

startTimer = timeit.default_timer()


def lista2():
    return range(1000)
L = lista2()
print(L) 
print("o tempo de execução é: ", timeit.default_timer() - startTimer)