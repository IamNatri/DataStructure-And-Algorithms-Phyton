import numpy as np

class vetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)
    
    #O(n)
    def imprime(self):
        if self.ultimaPosicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultimaPosicao +1):
                print(i, ' - ', self.valores[i])
    #O(n)                    
    def insere(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print('Capacidade maxima atingida')
            return
        
        #Buscando posição para inserir o novo valor
        posicao = 0
        for i in range(self.ultimaPosicao + 1):
            posicao = i
            #busca a posição do em que o valor atual é menor que o valor que se quer inserir
            if self.valores[i] > valor: 
                break
            #PESAQUISAR VETOR ORDENADO PARA LISTA COM DUPLICATA
            if i == self.ultimaPosicao:
                posicao = i+1
        
        #remanejando valores
        x = self.ultimaPosicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        
        self.valores[posicao] = valor
        self.ultimaPosicao += 1
    
    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao +1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i 
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range (posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
        self.ultimaPosicao -= 1 