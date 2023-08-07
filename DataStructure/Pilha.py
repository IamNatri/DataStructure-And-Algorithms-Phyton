import numpy as np

class pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        #privando o metodo de busca de valores para se ter acesso unicamente ao topo
        self.__valores = np.empty(self.__capacidade, dtype=int)
    
    #funcao auxiliar
    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False
    
    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha esta cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__pilha_vazia():
            print("A pilha esta vaiza")
        else:
            self.__topo -= 1
    
    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1
        