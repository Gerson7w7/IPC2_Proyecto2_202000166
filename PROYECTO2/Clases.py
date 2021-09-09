from EstructuraDatos import Cola, LinkedList

class Maquina(object):
    def __init__(self):
        self.cLineas = None
        self.lLineas = None
        self.lProductos = None


class LineaProduccion(object):
    def __init__(self, numero, cComponentes, tEnsamblaje):
        self.numero = numero
        self.cComponentes = cComponentes
        self.tEnsamblaje = tEnsamblaje
        self.usado = False
        self.componentesU = Cola()
        self.contador = 0


class Producto(object):
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion
        self.tiempos = LinkedList()
        self.tiempoT = 0


class Elaboracion(object):
    def __init__(self, l, c):
        self.l = l
        self.c = c
    
    def __str__(self):
        return str(self.l) + "-" + str(self.c)


class Simulacion(object):
    def __init__(self):
        self.nombre = None
        self.lProductos = None # solo nombres de los productos


class Tiempo(object):
    def __init__(self, segundo, lEnsamblaje, descripcion):
        self.segundo = segundo
        self.lEnsamblaje = lEnsamblaje
        self.descripcion = descripcion