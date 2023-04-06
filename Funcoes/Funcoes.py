def CalculoEnergiaPotencialGravitacional(m, h, g = 10):
    '''
    Calcula a energia potencial gravitacional
    Argumentos:
    m: massa, entrada como uma variável float
    h: altura, entrada como uma variável float

    Argumento opcional:
    g: aceleração gravitacional, com valor default de 10
    '''
    e = m * h * g
    return e

#help(CalculoEnergiaPotencialGravitacional)

CalculoEnergiaPotencialGravitacional(30, 12, 9.8)