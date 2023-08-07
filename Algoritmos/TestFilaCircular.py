from implementacao.FilaCircular import FilaCircular

fila = FilaCircular(5)

#== 5 4 3 2 1 ==
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

#== 5 4 3 2  ==
fila.desenfileirar()
#== 2 ==
fila.primeiro()
#== 5 4 3 ==
fila.desenfileirar()

#== 6 7 5 4 3 == 
fila.enfileirar(6)
fila.enfileirar(7)
#== array([6, 7, 3, 4, 5]) ==
fila.valores
#== index 2 ==
fila.inicio
#== index 1 ==
fila.final