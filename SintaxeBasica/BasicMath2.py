#calculo de consumo# 
    #km/l#
consumoConstante = 12
print('Digite o Tempo gasto na viagem em horas: ')
tempoViagem = int(input())

print('Digite a velocidade média, em km/h, da viagem: ')
velocidadeMedia = int(input())

    #Calculo distancia#
distancia = tempoViagem*velocidadeMedia

litrosUsados = distancia/consumoConstante

print('Quantidade de litros de gasolina gastos é: ', litrosUsados)

