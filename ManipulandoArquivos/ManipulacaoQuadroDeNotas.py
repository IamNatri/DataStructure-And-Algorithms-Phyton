alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('C:/Users/matheusb/Documents/Cursos/EstruturaDeDados/ManipulandoArquivos/QuadroDeNotas.txt', 'w') as QDN:
    QDN.write("Nome Aluno | Nota \n")
    for chave, valor in alunos.items():
        QDN.write(f'{chave} | {str(valor)} \n')
    

