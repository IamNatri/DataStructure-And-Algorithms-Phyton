import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_Elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def __fila_vazia(self):
        return self.numero_Elementos == 0
    
    def __fila_cheia(self):
        return self.numero_Elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila esta cheia!')
            return
        
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1 
        self.valores[self.final] = valor
        self.numero_Elementos += 1
    
    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila já esta vazia')
            return
        
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_Elementos -= 1
        return temp
    
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]
    



