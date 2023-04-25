import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.__valores = np.chararray(self.capacidade, unicode=True)
    
    #funcao auxiliar
    def __pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False
    
    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha esta cheia")
        else:
            self.__topo += 1
            self.__valores[self.topo] = valor
    
    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha esta vaiza")
        else:
            self.topo -= 1
    
    def ver_topo(self):
        if self.topo != -1:
            return self.__valores[self.topo]
        else:
            return -1
        

