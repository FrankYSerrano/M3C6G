import clases as c
import funciones as f
import random

#punto 3 y 4: Carga de datos a variables
with open("M3C6G\data\datos1.xml") as datos:
    datos1 = datos.read() 
#print(datos1)
with open("M3C6G\data\datos2.json") as datos:
    datos2 = datos.read() 
#print(datos2)
with open("M3C6G\data\datos3.csv") as datos:
    datos3 = datos.read() 
#print(datos3)
with open("M3C6G\data\datos4.txt") as datos:
    datos4 = datos.read() 
#print(datos4)

#Punto 5: Unificar todos los datos en una sola estructura 
datos_total = datos1 + datos2 + datos3 + datos4
print(datos_total)

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
