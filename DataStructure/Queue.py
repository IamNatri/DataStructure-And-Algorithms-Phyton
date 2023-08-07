import numpy as np
class Deque:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = -1
        self.__final = 0
        self.__numero_elementos = 0
        self.__valores = np.empty(self.__capacidade, dtype= int)

    def __deque_cheio(self):
        return (self.__inicio == 0 and self.__final == self.__capacidade -1) or (self.__inicio == self.__final + 1)
    
    
    def __deque_vazio(self):
        return self.__inicio == -1
    
    def insere_inicio (self, valor):
        if self.__deque_cheio():
            print('DEQUE ESTA CHEIO')
            return
        
        # se vazio
        if self.__inicio == -1:
            self.__inicio = 0
            self.__final = 0
        elif self.__inicio == 0:
            self.__inicio = self.__capacidade-1
        else:
            self.__inicio -= 1 
        
        self.__valores[self.__inicio] = valor
    
    def insere_final(self, valor):
        if self.__deque_cheio():
            print('DEQUE ESTA CHEIO')
            return
        # se vazio
        if self.__inicio == -1:
            self.__inicio = 0
            self.__final = 0
        elif self.__final == self.__capacidade -1:
            self.__final = 0
        else:
            self.__final += 1
        
        self.__valores[self.__final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque ja esta vazio')
            return
        
        #Possui somente um elemento
        if self.__inicio == self.__final:
            self.__inicio = -1
            self.__final = -1
        else:
            #voltando para a posição inicial
            if self.__inicio == self.__capacidade -1:
                self.__inicio = 0
            else:
                # incrementa 
                self.__inicio += 1
    
    def exclui_final(self):
        if self.__deque_vazio():
            print('O deque ja esta vazio')
            return        

        if self.__inicio == self.__final:
            self.__inicio= -1
            self.__final = -1
        elif self.__inicio == 0:
            self.__final = self.__capacidade -1
        else:
            self.__final -= 1
    
    def get_inicio(self):
        if self.__deque_vazio():
            print("Deque ja  esta vazio")
            return
        
        return self.__valores[self.__inicio]

    def get_final(self):
        if self.__deque_vazio() or self.__final < 0:
            print("Deque ja  esta vazio")
            return
        
        return self.__valores[self.__final]