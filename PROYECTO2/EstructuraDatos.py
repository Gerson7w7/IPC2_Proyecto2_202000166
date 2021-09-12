#=============================================CLASE NODO====================================================
class Nodo(object):
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


#=============================================CLASE LISTA ENALZADA=============================================    
class LinkedList(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0


    def append(self, dato): # función para agregar un dato
        nodo = Nodo(dato) 
        if self.cabeza: 
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else: # si es el primer dato
            self.cabeza = nodo
            self.cola = nodo
        self.size += 1


    def iterate(self): # función para iterar la lista
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
        
    # forma de llamar a la iteración:
    # for l in lista.iterate():
    #   print(l)    

    # función para obtener la cabeza de la cola
    def getCabeza(self):
        return self.cola.dato
        

    # función para eliminar al primer dato (la cabeza de la cola)    
    def pop(self):
        if not self.cabeza:
            return False
        else:
            actual = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return True


    # función buscar por índice
    def __getitem__(self, indice): 
        # si está entre 0 y el tamaño de la lista
        # devuelve el objeto
        if indice >= 0 and indice < self.size:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            return actual.dato
        else:
            return "Índice fuera de rango"

    # función que elimina un dato por medio del nombre del terreno
    def remove(self, dato):
        actual = self.cola
        anterior = self.cola
        while actual:
            if actual.dato.nombre == dato:
                if actual == self.cola:
                    self.cola = actual.siguiente
                else:
                    # esta línea es importante, ya que aquí se enlaza
                    # el anterior nodo con el siguiente nodo, así 
                    # remueve la conexción del nodo actual
                    anterior.siguiente = actual.siguiente
                self.size -= 1
                return
            anterior = actual
            actual = actual.siguiente

    # sobre escritura de la función len, para que devuelva el tamaño de la lista
    def __len__(self):
        return self.size


#=============================================CLASE COLA====================================================
class Cola(object): # clase cola
    def __init__(self):
        self.cabeza = None

    # función para agregar un dato
    def agregar(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato)
            return True
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato)
            return True
        
    # función para eliminar al primer dato (la cabeza de la cola)    
    def eliminar(self):
        if not self.cabeza:
            return False
        else:
            actual = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return True
    
    # función para obtener la cabeza de la cola
    def getCabeza(self):
        if not self.cabeza:
            return None
        else:
            return self.cabeza.dato
    
    # función para obtener la cola de la fila
    def getCola(self):
        actual = self.cabeza
        while(actual.siguiente):
            actual = actual.siguiente
        return actual.dato

    def vacio(self):
        if not self.cabeza:
            return True
        else:
            return False

    # función para imprimir la cola
    def imprimir(self):
        lista = ""
        actual = self.cabeza
        while(actual):
            lista = "%s%s%s" % (lista, "\n", actual.dato)
            actual = actual.siguiente
        lista = "%s" % (lista)
        print(lista)


    def iterate(self):
        actual = self.cabeza
        while(actual):
            dato = actual.dato
            actual = actual.siguiente
            yield dato