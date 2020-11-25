import csv
import clases as c
import funciones as f
import random
#import xml.sax.handler
#import xml.sax

#punto 3 y 4: Carga de datos a variables
with open("data\datos1.xml") as datos:
    datos1 = datos.read() 
#print(datos1)
with open("data\datos2.json") as datos:
    datos2 = datos.read() 
#print(datos2)
with open("data\datos3.csv", "r") as datos:
#    datos3 = datos.read()
    datos3 = csv.reader(datos)
    for linea in datos3:
        print(linea)

with open("data\datos8.csv", mode="w") as datos:
#    datos3 = datos.write()
#    encabezados = csv.writer(datos, delimiter=',')
    encabezados = ['EncA', 'EncB', 'EncC']
    writer = csv.DictWriter(datos, fieldnames = encabezados)
    writer.writeheader()
    writer.writerow({"EncA": "ABC", "EncB": "PEPE", "EncC": "xxx"})
    writer.writerow({"EncA": "DEF", "EncB": "FAFA", "EncC": "yyy"})
#    datosx.writerrow()
#    datos3 = csv.reader(datos)
#    for linea in datosx:
#        print(linea)


#print(datos3)
with open("data\datos4.txt") as datos:
    datos4 = datos.read() 
#print(datos4)

#Punto 5: Unificar todos los datos en una sola estructura 

#Ciclo que recorra datos1 XML 
# usando getElementsByTagName(NOMBRE) + getElementsByTagName(APELLIDO) + getElementsByTagName(OTRO)
# Append a "datos_total"

#Ciclo que recorra datos2 JSON/DICCIONARIO 
# buscando por ID y extrayendo el valor de (NOMBRE) + (APELLIDO) + (OTRO)
# Append a "datos_total"

#Ciclo que recorra datos3 CSV 
# Usando linea.split(",") y extrayendo los elementos (NOMBRE) + (APELLIDO) + (OTRO) asociados a de la lista generada
# Append a "datos_total"

#Ciclo que recorra datos3 TXT 
# Usando linea.split(" ") y extrayendo los elementos (NOMBRE) + (APELLIDO) + (OTRO) asociados a de la lista generada
# Append a "datos_total"
'''
from xml.etree.ElementTree import parse
xml_docx = parse('data\profe.xml')
#print(xml_doc)
print(dir(xml_docx))
#print(help(xml_docx))
a = xml_docx.itemfind("Nombre")
print(a)

#b = xml_docx.findtext('Nombre')
#print(b)

#for ele in xml_doc.find('titulo'):
#for ele in xml_doc.findtext('titulo'):
#    print(ele.text)

print("termine")

class AlbumSaxHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.in_title = False
    def startElement(self, name, attributes):
        if name == 'titulo':
            self.in_title = True
    def characters(self, data):
        if self.in_title:
            print(data)
    def endElement(self, name):
        if name == 'titulo':
            self.in_title = False

parser = xml.sax.make_parser()
sax_handler = AlbumSaxHandler()
parser.setContentHandler(sax_handler)
parser.parse(datos1)

'''



#datos_total = datos1 + datos2 + datos3 + datos4
#print(datos_total)



'''
5. Unificar todos los datos en una sola estructura llamada datos_total.
Para esto deberá tener cuidado de no mezclar nombres de columnas
entre los distintos conjuntos de datos provenientes de diferentes
archivos.
6. Mostrar los datos en pantalla con aspecto de tabla con títulos de
columnas.
7. Realizar una copia de los datos a otra variable que contenga solo las
primeras 4 columnas de los datos.
8. Cree 3 nuevas columnas, a la derecha de las 4 existentes, llamadas
‘max’, ‘min’, ‘promedio’.
9. Llene esas columnas con los valores máximos, mínimos y promedio
de cada fila, respectivamente.
10. Calcule y muestre en pantalla el valor máximo, mínimo y
promedio de cada una de las primeras 4 columnas.
11. Muestre en pantalla la tabla completa actualizada.
12. Guarde los datos resultantes en 4 archivos diferentes, con
formatos XML, JSON, CSV y Separado por expacios.
13. Deje sus resultados en el repositorio GitHub del ejercicio.
'''
