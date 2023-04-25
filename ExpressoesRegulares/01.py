import re

texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"
numeros = re.findall('\d', texto)
CEP = re.findall('\d{5}\-{1}\d{3}',texto)
URL = re.findall('https?://[A-Za-z0-9./]+',texto)
print(numeros)
print(CEP)
print(URL)