#==========Conjuntos(set)=========

biomeleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')
print(biomeleculas)
    #Tras somente os elementos que não se repetem, únicos.
print("Print com 'set()': ", set(biomeleculas))

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
    #realiza intersecção de conjuntos
c3 = c1.intersection(c2)
print(c3)
    #esta no conjunto 1 mas não esta no conjunto 2
c4 = c1.difference(c2)
print(c4)