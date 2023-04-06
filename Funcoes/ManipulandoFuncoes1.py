def interfaceConversao():
    temperaturaFahrenheit = recebeValores()
    Informa(temperaturaFahrenheit)

def recebeValores():
    temperaturaCelcius = int(input("informe a temperatura °C para conversão em °F: "))
    return calculoConversao(temperaturaCelcius)

def calculoConversao(C):
    F = (9 * C + 160) / 5
    return F

def Informa(T):
    return print(T, "°F")

interfaceConversao()