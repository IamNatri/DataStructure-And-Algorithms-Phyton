#======DICIONARIO========#
#Funciona no estilo chave-valor, dicionario = {chave1: valor1, .... , chave'n' : valor'n'}
coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta)
print(coleta['Aedes aegypt'])

print("-----------")
del(coleta)['Aedes albopictus']
print(coleta)

print("-----------")
print(coleta.items())

print("-----------")
print(coleta.keys())

print("-----------")
print(coleta.values())

print("-----------")
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
coleta.update(coleta2)
print(coleta)

#para o for teremos que usar duas variaveis a primeira percorre a chave a segunda pega o valor

for especie, numeroEspecimes in coleta.items():
    print(f'Espécie: {especie}, numéro de espécimes coletados: {numeroEspecimes}')
