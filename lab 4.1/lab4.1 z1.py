moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
moja_lista_2 = [1,3,5]
print(moja_lista)
print(moja_lista[0])
print(moja_lista[-1])
print(len(moja_lista))
print(max(moja_lista))
print(min(moja_lista))
print(sum(moja_lista))
print(sorted(moja_lista))
moja_lista.append(6)
print(moja_lista)
moja_lista.insert(0,5)
print(moja_lista)
print(moja_lista.pop())
moja_lista.reverse()
print(moja_lista)
moja_listaL = moja_lista + moja_lista_2
print(moja_listaL)
moja_listaL = moja_lista*5
print(moja_listaL)
print(moja_listaL[:3])
print(moja_listaL[5:])
print(moja_listaL[1:8:2])
print(moja_listaL[::-1])