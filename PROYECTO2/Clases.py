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


class Producto(object):
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion


class Elaboracion(object):
    def __init__(self, l, c):
        self.l = l
        self.c = c