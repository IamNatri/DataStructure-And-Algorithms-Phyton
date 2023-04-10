with open('C:/Users/matheusb/Documents/Cursos/EstruturaDeDados/ManipulandoArquivos/1.SQL', 'r') as text:

    r = text.readlines()
    print(r)

with open('C:/Users/matheusb/Documents/Cursos/EstruturaDeDados/ManipulandoArquivos/texto.txt', 'w') as texto:
    texto.write("ola mundo")
    texto.write("\n")
    texto.write("olá novamente")

with  open('C:/Users/matheusb/Documents/Cursos/EstruturaDeDados/ManipulandoArquivos/texto.txt', 'r') as texto:
    for linhas1 in texto:
        print (linhas1)
