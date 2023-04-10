class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0
    
    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2)/2
        return self.media 
    
    def mostraDados(self):
        print("nome: ", self.nome)
        print("nota 1: ", self.nota1)
        print("nota 2: ", self.nota2)
        print("Média: ", self.calcularMedia())
        
        return 
    
    def status(self):
        if (self.nota1/self.nota2)/2 < 6:
            print("Reprovado!")
        else:
            print("Aprovado!")


matheus = aluno("matheus", 6,5)
matheus.mostraDados()

matheus.calcularMedia()

#matheus.status()



