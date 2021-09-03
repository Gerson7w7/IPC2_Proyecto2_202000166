import xml.dom.minidom 
from Clases import *

# instanciando un objeto de tipo máquina
maquina = Maquina()

def analizarConfig(archivo):
    xmlDoc = xml.dom.minidom.parse(archivo) # para manejar el xml con las etiquetas
    data = xmlDoc.documentElement

    # cantidad de linea de producción
    clp = data.getElementsByTagName("CantidadLineasProduccion")[0]
    maquina.cLinea = int(clp.firstChild.data)
    print(maquina.cLinea)

    # lista de las linea de las linea de producción
    llp = data.getElementsByTagName("ListadoLineasProduccion")[0] 
    lp = llp.getElementsByTagName("LineaProduccion")
    for l in lp:
        # numero de la linea de producción
        Numero = l.getElementsByTagName("Numero")[0] 
        numero = int(Numero.firstChild.data)
        print(numero)

        # cantidad de componentes
        cc = l.getElementsByTagName("CantidadComponentes")[0]
        cComponentes = int(cc.firstChild.data)
        print(cComponentes)

        # tiempo de ensamblaje
        te = l.getElementsByTagName("TiempoEnsamblaje")[0]
        tEnsamblaje = int(te.firstChild.data)
        print(tEnsamblaje)

        # metiendo cada linea de producción a una lista enlazada
    
    # lista de los productos 
    lp = data.getElementsByTagName("ListadoPorductos")[0]
    producto = lp.getElementsByTagName("Producto")
    for p in producto:
        # nombre del producto
        n = p.getElementsByTagName("nombre")[0] #-------------------------------POSIBLE CAMBIO-----------------------------------
        nombre = n.firstChild.data
        nombre = nombre.strip()
        print(nombre)

        # elaboración (serie de pasos)
        e = p.getElementsByTagName("elaboracion")[0] #-------------------------------POSIBLE CAMBIO--------------------------------
        elaboracion = e.firstChild.data
        elaboracion = elaboracion.strip()
        print(elaboracion)

        # metiendo cada producto en una lista enlazada
    

def analizarSimulacion(archivo):
    xmlDoc = xml.dom.minidom.parse(archivo) # para manejar el xml con las etiquetas
    data = xmlDoc.documentElement
    # nombre de la simulación
    n = data.getElementsByTagName("Nombre")[0]
    nombre = n.firstChild.data
    print(nombre)

    # listado de productos
    lp = data.getElementsByTagName("ListadoProductos")[0]
    lproducto = lp.getElementsByTagName("Producto")
    for p in lproducto:
        # nombre del producto a ensamblar
        producto = p.firstChild.data
        print(producto)

