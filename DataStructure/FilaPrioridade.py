import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
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
        
        if self.numero_Elementos == 0:
            self.valores[self.numero_Elementos] = valor
            self.numero_Elementos += 1 
        else:
            x = self.numero_Elementos -1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
                x -= 1
                self.valores[x+1] = valor 
                self.numero_Elementos +=1


    
    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila já esta vazia')
            return
        
        valor = self.valores[self.numero_Elementos -1 ]
        self.numero_Elementos -=1
        return valor
        
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_Elementos - 1]
    



