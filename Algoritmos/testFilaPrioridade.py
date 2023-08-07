from implementacao.FilaPrioridade import FilaPrioridade

fila = FilaPrioridade(10)
print(fila.primeiro())


fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
print(fila.primeiro())
fila.enfileirar(5)

print(fila.primeiro())
print(fila.valores)
