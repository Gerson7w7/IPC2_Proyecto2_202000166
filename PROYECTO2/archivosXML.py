import xml.dom.minidom 
from Clases import *
from EstructuraDatos import LinkedList, Cola

# instanciando un objeto de tipo máquina
maquina = Maquina()
def analizarConfig(archivo):
    xmlDoc = xml.dom.minidom.parse(archivo) # para manejar el xml con las etiquetas
    data = xmlDoc.documentElement

    # cantidad de linea de producción
    clp = data.getElementsByTagName("CantidadLineasProduccion")[0]
    maquina.cLinea = int(clp.firstChild.data)

    # lista de las linea de las linea de producción
    llp = data.getElementsByTagName("ListadoLineasProduccion")[0] 
    lp = llp.getElementsByTagName("LineaProduccion")
    # creando una lista enlazada para guardar las linea de producción
    lLineas = LinkedList()
    for l in lp:
        # numero de la linea de producción
        Numero = l.getElementsByTagName("Numero")[0] 
        numero = int(Numero.firstChild.data)

        # cantidad de componentes
        cc = l.getElementsByTagName("CantidadComponentes")[0]
        cComponentes = int(cc.firstChild.data)

        # tiempo de ensamblaje
        te = l.getElementsByTagName("TiempoEnsamblaje")[0]
        tEnsamblaje = int(te.firstChild.data)

        # metiendo cada linea de producción a una lista enlazada
        lLineas.append(LineaProduccion(numero, cComponentes, tEnsamblaje))
    # asignando la lista de lineas a la máquina
    maquina.lLineas = lLineas 

    # lista de los productos 
    lp = data.getElementsByTagName("ListadoProductos")[0]
    producto = lp.getElementsByTagName("Producto")
    # creando una lista enlazada para los productos
    lProductos = LinkedList()
    for p in producto:
        # nombre del producto
        n = p.getElementsByTagName("nombre")[0]
        nombre = n.firstChild.data
        nombre = nombre.strip()

        # elaboración (serie de pasos)
        e = p.getElementsByTagName("elaboracion")[0]
        elaboracion = e.firstChild.data
        elaboracion = elaboracion.strip()
        elaboracion = pasos(elaboracion)

        # metiendo cada producto en una lista enlazada
        lProductos.append(Producto(nombre, elaboracion))
    # asignando la lista de productos a la máquina
    maquina.lProductos = lProductos 

    # probando...
    for l in maquina.lLineas.iterate():
        print(l.numero)

    for l in maquina.lProductos.iterate():
        print(l.nombre)
        l.elaboracion.imprimir()


# procesando la elaboracion pasando de un string a una cola
def pasos(elaboracion):
    aux = Cola()
    elaboracion = elaboracion.split(" ")
    for e in elaboracion:
        l = e[:2]
        c = e[-2:]
        aux.agregar(Elaboracion(l, c))
    return aux


# instanciando un objeto de tipo simulación
simulacion = Simulacion()
# lista enlazada de los nombres de los productos a ensamblar
lProductos = LinkedList()
def analizarSimulacion(archivo):   
    xmlDoc = xml.dom.minidom.parse(archivo) # para manejar el xml con las etiquetas
    data = xmlDoc.documentElement
    # nombre de la simulación
    n = data.getElementsByTagName("Nombre")[0]
    nombre = n.firstChild.data
    nombre = nombre.strip()
    simulacion.nombre = nombre

    # listado de productos
    lp = data.getElementsByTagName("ListadoProductos")[0]
    lproducto = lp.getElementsByTagName("Producto")
    for p in lproducto:
        # nombre del producto a ensamblar
        producto = p.firstChild.data
        producto = producto.strip()
        lProductos.append(producto)
    # agregando los atributos al objeto simulación
    simulacion.lProductos = lProductos
    print(len(simulacion.lProductos))