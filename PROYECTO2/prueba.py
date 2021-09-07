from EstructuraDatos import Cola

cola = Cola()

cola.agregar("hola")
cola.agregar("1")
cola.agregar("2")
cola.agregar("3")

cola.imprimir()

for c in cola.iterate():
    print(c)