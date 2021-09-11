import xml.dom.minidom 
from Clases import *
from EstructuraDatos import LinkedList

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
    for l in maquina.lProductos.iterate():
        print(l.elaboracion.getCabeza())


# procesando la elaboracion pasando de un string a una cola
def pasos(elaboracion):
    aux = Cola()
    elaboracion = elaboracion.split(" ")
    for e in elaboracion:
        l = int(e[1])
        c = int(e[3])
        aux.agregar(Elaboracion(l, c))
    return aux


# instanciando un objeto de tipo simulación
simulacion = Simulacion()
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
    # lista enlazada de los nombres de los productos a ensamblar
    lProductos = LinkedList()
    for p in lproducto:
        # nombre del producto a ensamblar
        producto = p.firstChild.data
        producto = producto.strip()
        lProductos.append(producto)
    # agregando los atributos al objeto simulación
    simulacion.lProductos = lProductos
    ejecSimulacion()

# nombre de la simulación para usarlo en el archivo salida
def ejecSimulacion():
    for s in simulacion.lProductos.iterate():
        for producto in maquina.lProductos.iterate():
            if s == producto.nombre:
                elaboracion(producto)
                crearArchivoSimulacion(False, "", 0)
                break

# productos ensamblados individualmente
productoIndividual = LinkedList()
def ensambladoP(productoN, numEnsamblado):
    for producto in maquina.lProductos.iterate():
        if productoN == producto.nombre:
            repetido = False
            if len(productoIndividual) != 0:
                for p in productoIndividual.iterate():
                    if producto.nombre == p.nombre:
                        repetido = True
            if not repetido:
                productoIndividual.append(producto)
            if producto.tiempoT == 0:
                elaboracion(producto)
            crearArchivoSimulacion(True, producto, numEnsamblado)
            return producto


def elaboracion(producto):
    lineasUsadas = LinkedList()
    # lista de elaboración o pasos por cada producto
    for e in producto.elaboracion.iterate():
        # lista de lineas de produccion de la maquina
        for linea in maquina.lLineas.iterate():
            if len(lineasUsadas) == 0:
                if e.l == linea.numero:
                    linea.usado = True
                    linea.componentesU.agregar(e.c)
                    lineasUsadas.append(linea)
                    print("linea nueva: " + str(linea.numero))
                    break 
            else:
                if e.l == linea.numero and linea.usado == False:
                    linea.usado = True
                    linea.componentesU.agregar(e.c)
                    lineasUsadas.append(linea)
                    print("linea nueva: " + str(linea.numero))
                    break     
                elif e.l == linea.numero and linea.usado == True:
                    linea.componentesU.agregar(e.c)
                    break
    
    # tiempo en segundos de la elaboración
    t = 1
    tEnsamblaje = 1
    while(not producto.elaboracion.vacio()):
        e = producto.elaboracion.getCabeza()
        for linea in lineasUsadas.iterate():
            # si llega al componente que tiene que ensamblar
            if linea.componentesU.getCabeza() != None:
                if linea.componentesU.getCabeza() == linea.contador:
                    # si es igual a la cabeza de la elaboracion
                    if e.l == linea.numero and e.c == linea.contador:
                        # mientas sea menor al tiempo de ensamblaje
                        if tEnsamblaje < linea.tEnsamblaje:
                            descripcion = "Se ensamblo el componente " + str(linea.componentesU.getCabeza())
                            producto.tiempos.append(Tiempo(t, linea.numero, descripcion))
                            print(t, linea.numero, descripcion)
                            tEnsamblaje += 1
                        elif tEnsamblaje == linea.tEnsamblaje:
                            descripcion = "Se ensamblo el componente " + str(linea.componentesU.getCabeza())
                            producto.tiempos.append(Tiempo(t, linea.numero, descripcion))
                            print(t, linea.numero, descripcion)
                            tEnsamblaje = 1
                            producto.elaboracion.eliminar()
                            linea.componentesU.eliminar()
                    # si llego al componente pero no le toca ser ensamblado
                    elif linea.componentesU.getCabeza() == linea.contador:
                        descripcion = "No se hizo nada"
                        producto.tiempos.append(Tiempo(t, linea.numero, descripcion))
                        print(t, linea.numero, descripcion)
                else:
                    # si el componente al que tiene que llegar es mayor al actual
                    if linea.componentesU.getCabeza() > linea.contador:
                        linea.contador += 1
                        descripcion = "Se movio el brazo al componente " + str(linea.contador)
                        producto.tiempos.append(Tiempo(t, linea.numero, descripcion))
                        print(t, linea.numero, descripcion)
                    elif linea.componentesU.getCabeza() < linea.contador:
                        linea.contador -= 1
                        descripcion = "Se movio el brazo al componente " + str(linea.contador)
                        producto.tiempos.append(Tiempo(t, linea.numero, descripcion))
                        print(t, linea.numero, descripcion)
            else:
                descripcion = "No se hizo nada"
                producto.tiempos.append(Tiempo(t, linea.numero, descripcion))
                print(t, linea.numero, descripcion)
        # aumentamos un segundo en el tiempo una vez haya pasado por todas la lineas
        t += 1
    # tiempo total de la elaboración del producto
    producto.tiempoT = t - 1 
        
    # reiniciando las lineas para el siguiente productos de
    for lineaUsada in lineasUsadas.iterate():
        lineaUsada.usado = False  
        lineaUsada.contador = 0
    print("nuevo producto")        


def crearArchivoSimulacion(individual, productoI, numEmulacion):
    # creando el archivo xml
    DOMimp = xml.dom.minidom.getDOMImplementation()
    xmlDoc = DOMimp.createDocument(None, "SalidaSimulacion", None)
    # raíz del archivo
    docRoot = xmlDoc.documentElement

    # nombre de la simulación
    nombre = xmlDoc.createElement("Nombre")
    if individual:
        nombre.appendChild(xmlDoc.createTextNode("Simulacion Individual"))
    else:    
        nombre.appendChild(xmlDoc.createTextNode(simulacion.nombre))
    docRoot.appendChild(nombre)

    # nodo Listado de productos
    lp = xmlDoc.createElement("ListadoProductos")

    if individual:
        # nodo producto
        p = xmlDoc.createElement("Producto")

        # sub nodo nombre
        n = xmlDoc.createElement("Nombre")
        n.appendChild(xmlDoc.createTextNode(str(productoI.nombre)))
        p.appendChild(n)

        # sub nodo tiempo total
        tt = xmlDoc.createElement("TiempoTotal")
        tt.appendChild(xmlDoc.createTextNode(str(productoI.tiempoT)))
        p.appendChild(tt)

        # sub nodo elaboración optima
        eo = xmlDoc.createElement("ElaboracionOptima")
        tAux = 1
        while(tAux <= productoI.tiempoT):
            aux = LinkedList()            
            for tiempo in productoI.tiempos.iterate():
                if tAux == tiempo.segundo:
                    aux.append(tiempo)

            # sub nodo de tiempo
            t = xmlDoc.createElement("Tiempo")
            t.setAttribute("NoSegundo", str(tAux))
            # sub nodo linea de ensamblaje y descripcion
            for tiempo in aux.iterate():
                le = xmlDoc.createElement("LineaEnsamblaje")
                le.setAttribute("NoLinea", str(tiempo.lEnsamblaje))
                le.appendChild(xmlDoc.createTextNode(str(tiempo.descripcion)))
                t.appendChild(le)
            eo.appendChild(t)
            tAux += 1
        p.appendChild(eo)
        lp.appendChild(p)
    else:
        # por cada producto creamos un nodo
        for producto in maquina.lProductos.iterate():          
            if len(producto.tiempos) != 0:
                # nodo producto
                p = xmlDoc.createElement("Producto")

                # sub nodo nombre
                n = xmlDoc.createElement("Nombre")
                n.appendChild(xmlDoc.createTextNode(str(producto.nombre)))
                p.appendChild(n)

                # sub nodo tiempo total
                tt = xmlDoc.createElement("TiempoTotal")
                tt.appendChild(xmlDoc.createTextNode(str(producto.tiempoT)))
                p.appendChild(tt)

                # sub nodo elaboración optima
                eo = xmlDoc.createElement("ElaboracionOptima")
                tAux = 1
                while(tAux <= producto.tiempoT):
                    aux = LinkedList()            
                    for tiempo in producto.tiempos.iterate():
                        if tAux == tiempo.segundo:
                            aux.append(tiempo)

                    # sub nodo de tiempo
                    t = xmlDoc.createElement("Tiempo")
                    t.setAttribute("NoSegundo", str(tAux))
                    # sub nodo linea de ensamblaje y descripcion
                    for tiempo in aux.iterate():
                        le = xmlDoc.createElement("LineaEnsamblaje")
                        le.setAttribute("NoLinea", str(tiempo.lEnsamblaje))
                        le.appendChild(xmlDoc.createTextNode(str(tiempo.descripcion)))
                        t.appendChild(le)
                    eo.appendChild(t)
                    tAux += 1
                p.appendChild(eo)
                lp.appendChild(p)

    # añadimos el nodo terreno a la raíz del archivo
    docRoot.appendChild(lp)

    # guardando el fichero en la ruta especificada
    if individual:
        ruta = f"Archivos de Salida/SimulacionIndividual_{numEmulacion}.xml"
    else:
        ruta = f"Archivos de Salida/Simulacion_{simulacion.nombre}.xml"
    archivo = open(ruta, 'w')
    archivo.write(xmlDoc.toxml())
    archivo.close()
    print("Se ha escrito el archivo con éxito! :D")