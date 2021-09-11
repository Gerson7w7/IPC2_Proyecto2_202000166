import os
from archivosXML import maquina

def grafica():
    for producto in maquina.lProductos.iterate():
        archivo = open("grafo.dot", "w")
        archivo.write("digraph grafo{\n")
        archivo.write(f"label={producto.nombre}\n")
        cadena = ""
        for e in producto.elaboracion.iterate():
            if e.c == producto.elaboracion.getCola().c and e.l == producto.elaboracion.getCola().l:
                cadena += f"L{e.l}C{e.c};\n"
            else:
                cadena += f"L{e.l}C{e.c} -> "
        archivo.write(cadena)
        archivo.write("rankdir=LR;\n")

        archivo.write("}")
        archivo.close()
        os.system(f'cmd /c "dot.exe -Tpng grafo.dot -o Graphviz/{producto.nombre}.png"')