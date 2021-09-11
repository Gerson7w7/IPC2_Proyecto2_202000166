from archivosXML import maquina, simulacion, productoIndividual
from EstructuraDatos import LinkedList

def repSimulacion():
    html = open(f"Reportes/Simulacion_{simulacion.nombre}.html", 'w')
    html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
            + '<html>'
            + '<!--Encabezado-->'
            + '<head>'
            + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
            + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
            + '<meta name="description" content="name"><!--autor de la pagina-->'
            + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
            + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
            + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
            + '<link rel="stylesheet" type="text/css" href="css/styles.css"/><!--css /estilo/tipo/ruta relativa -->'
            + '<title>Reporte Simulación</title><!--Titulo visible de la pagina-->'
            + '</head>'
            + '<body>'
            + '<center><!--centra todos lo que este dentro-->')
    
    for producto in maquina.lProductos.iterate():   
        html.write(f'<h6 class="titulos"><b> {producto.nombre} </b></h6>'
                + '<br>  <br>  <br>'
                + '<!----tabla 2-->'
                + '<table class="steelBlueCols">'
                + '<thead>'
                + '<tr> <th>Tiempo</th>')

        nLinea = 0
        for tiempo in producto.tiempos.iterate():
            if nLinea < tiempo.lEnsamblaje:
                nLinea = tiempo.lEnsamblaje

        for n in range(nLinea):
            html.write(f'<th>Linea {n + 1}</th>')     
        html.write('</tr>'
                + '</thead>'
                + '<tbody>')

        t = 1
        while(t <= producto.tiempoT):
            aux = LinkedList()
            for tiempo in producto.tiempos.iterate():
                if t == tiempo.segundo:
                    aux.append(tiempo)

            html.write(f'<tr> <td>{str(t)}</td>')
            linea = 1
            while(linea <= nLinea):
                flag = True
                for tiempo in aux.iterate():
                    if linea == tiempo.lEnsamblaje:
                        html.write(f'<td>{tiempo.descripcion}</td>') 
                        flag = False
                if flag:
                    html.write(f'<td>Linea apagada</td>') 
                linea += 1
            t += 1
            html.write('</tr>')
        
        html.write(f'<tr><td colspan="{nLinea + 1}">Tiempo total: {str(producto.tiempoT)}</td></tr>')

        html.write('</tbody>'
                + '</table>'
                + '<!----termina tabla 2-->')

    html.write('<br>  <br>  <br>'
            + '</center>'
            + '</body>'
            + '</html>')
    html.close()


def repIndividual():
    html = open("Reportes/SimulacionIndividual.html", 'w')
    html.write('<!DOCTYPE html><!--Declarar el tipo de cumento -->'
            + '<html>'
            + '<!--Encabezado-->'
            + '<head>'
            + '<meta charset="UTF-8"><!--codififcaion de caracteres ñ y á-->'
            + '<meta name="name" content="Reporte"><!--nombre de la pagina-->'
            + '<meta name="description" content="name"><!--autor de la pagina-->'
            + '<meta name="keywods" content="uno,dos,tres"><!--Palabras claavez para, separadas por comas-->'
            + '<meta name="robots" content="Index, Follow"><!--Mejora la busqueda-->'
            + '<meta name="viewport" content="width=device-width, initial-scale=1"><!--visibilidaad en diferentes pantallas -->'
            + '<link rel="stylesheet" type="text/css" href="css/styles.css"/><!--css /estilo/tipo/ruta relativa -->'
            + '<title>Simulación Individual</title><!--Titulo visible de la pagina-->'
            + '</head>'
            + '<body>'
            + '<center><!--centra todos lo que este dentro-->')
    
    for producto in productoIndividual.iterate():   
        html.write(f'<h6 class="titulos"><b> {producto.nombre} </b></h6>'
                + '<br>  <br>  <br>'
                + '<!----tabla 2-->'
                + '<table class="steelBlueCols">'
                + '<thead>'
                + '<tr> <th>Tiempo</th>')

        nLinea = 0
        for tiempo in producto.tiempos.iterate():
            if nLinea < tiempo.lEnsamblaje:
                nLinea = tiempo.lEnsamblaje

        for n in range(nLinea):
            html.write(f'<th>Linea {n + 1}</th>')     
        html.write('</tr>'
                + '</thead>'
                + '<tbody>')

        t = 1
        while(t <= producto.tiempoT):
            aux = LinkedList()
            for tiempo in producto.tiempos.iterate():
                if t == tiempo.segundo:
                    aux.append(tiempo)

            html.write(f'<tr> <td>{str(t)}</td>')
            linea = 1
            while(linea <= nLinea):
                flag = True
                for tiempo in aux.iterate():
                    if linea == tiempo.lEnsamblaje:
                        html.write(f'<td>{tiempo.descripcion}</td>') 
                        flag = False
                if flag:
                    html.write(f'<td>Linea apagada</td>') 
                linea += 1
            t += 1
            html.write('</tr>')
        
        html.write(f'<tr><td colspan="{nLinea + 1}">Tiempo total: {str(producto.tiempoT)}</td></tr>')

        html.write('</tbody>'
                + '</table>'
                + '<!----termina tabla 2-->')

    html.write('<br>  <br>  <br>'
            + '</center>'
            + '</body>'
            + '</html>')
    html.close()