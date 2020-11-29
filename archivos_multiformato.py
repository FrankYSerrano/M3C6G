import csv
import os
from xml.etree.ElementTree import parse
import json

#import pandas as pd
#import clases as c
#import funciones as f

#Punto 1: Se tomo el precio del dolar observado de Banco Central de Chil
#Punto 2: Se salvo esa matriz en los diferentes formatos requeridos
#Punto 3: Carga de datos a variables
with open("data\datos1.xml") as datos:
    datos1 = datos.read() 
with open("data\datos2.json") as datos:
    datos2 = datos.read() 
with open("data\datos3.csv") as datos:
    datos3 = datos.read()
with open("data\datos4.txt") as datos:
    datos4 = datos.read() 

#Punto 4: Impresion tal como se cargaron
#print(datos1)
#print(datos2)
print(datos3)
#print(datos4)

#Punto 5: Unificacion en datos_total
os.system("cls")

#Se almacenara todo en datos_total
datos_total = {'Día':[], 'Enero':[], 'Febrero':[], 'Marzo':[], 'Abril':[], 'Mayo':[],
                'Junio':[], 'Julio':[], 'Agosto':[], 'Septiembre':[], 
                'Octubre':[], 'Noviembre':[], 'Diciembre':[]}

#PROCESAR XML
document = parse('data\datos1.xml')
i=1
for item in document.iterfind('row'):
    datos_total['Día'].append(item.findtext('Día'))
    datos_total['Enero'].append(item.findtext('Enero'))
    datos_total['Febrero'].append(item.findtext('Febrero'))
    datos_total['Marzo'].append(item.findtext('Marzo'))
    datos_total['Abril'].append(item.findtext('Abril'))
    datos_total['Mayo'].append(item.findtext('Mayo'))
    datos_total['Junio'].append(item.findtext('Junio'))
    datos_total['Julio'].append(item.findtext('Julio'))
    datos_total['Agosto'].append(item.findtext('Agosto'))
    datos_total['Septiembre'].append(item.findtext('Septiembre'))
    datos_total['Octubre'].append(item.findtext('Octubre'))
    datos_total['Noviembre'].append(item.findtext('Noviembre'))
    datos_total['Diciembre'].append(item.findtext('Diciembre'))
#    print("Inclui la linea: ", i)
    i=i+1

#PROCESAR CSV
with open("data\datos3.csv") as datos:
    reader = csv.reader(datos)
    i = 1
    for linea in reader:
        if i > 2:
            datos_total['Día'].append(linea[0])
            datos_total['Enero'].append(linea[1])
            datos_total['Febrero'].append(linea[2])
            datos_total['Marzo'].append(linea[3])
            datos_total['Abril'].append(linea[4])
            datos_total['Mayo'].append(linea[5])
            datos_total['Junio'].append(linea[6])
            datos_total['Julio'].append(linea[7])
            datos_total['Agosto'].append(linea[8])
            datos_total['Septiembre'].append(linea[9])
            datos_total['Octubre'].append(linea[10])
            datos_total['Noviembre'].append(linea[11])
            datos_total['Diciembre'].append(linea[12])
        i = i + 1

#PROCESAR TXT
with open("data\datos4.txt") as datos:
    reader = csv.reader(datos,delimiter='alt+09')
    i = 1
    for linea in reader:
        if i > 2:
            datos_total['Día'].append(linea[0])
            datos_total['Enero'].append(linea[1])
            datos_total['Febrero'].append(linea[2])
            datos_total['Marzo'].append(linea[3])
            datos_total['Abril'].append(linea[4])
            datos_total['Mayo'].append(linea[5])
            datos_total['Junio'].append(linea[6])
            datos_total['Julio'].append(linea[7])
            datos_total['Agosto'].append(linea[8])
            datos_total['Septiembre'].append(linea[9])
            datos_total['Octubre'].append(linea[10])
            datos_total['Noviembre'].append(linea[11])
            datos_total['Diciembre'].append(linea[12])
        i = i + 1

print(datos_total['Día'])



'''
#PROCESAR JSON
document2 = open('data\datos2.json')

linea = document2.readline()
lineaT=""
for linea in document2:
#    print(linea)
    lineaT = lineaT + linea
#    print("***", data)
#print(lineaT)
#data = json.loads(lineaT)
'''
'''


document2.close()




#print(datos_total['Día'])



# Cierre de Archivos
#datos1.close()
#datos2.close()
#datos3.close()
#datos4.close()
'''