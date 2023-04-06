def interfaceConversao():
    litrosUsados = recebeValores()
    Informa(litrosUsados)

def recebeValores():
    tempoViagem = int(input("informe de quantas horas foi sua viagem: "))
    VelocidadeMedia = int(input("informe sua velocidade média durante a viagem: "))
    return calculoConversao(tempoViagem, VelocidadeMedia)

def calculoConversao(t,v):
    distancia = t * v
    return distancia / 12

def Informa(T):
    return print(T, "Litos de conbustivel")

interfaceConversao()