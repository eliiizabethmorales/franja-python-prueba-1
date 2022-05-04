#  Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#  Escribe un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después tu programa debe mostrar el precio habitual de una barra de pan,
#  el descuento que se le hace por no ser fresca y el coste final total.

#solucion ejercicio1:

panañejo = int(input("hola cuantas barras de pan lleva que no son de hoy:"))
pandehoy = 3.49
pandeayer = 1.40
descuento = (pandehoy * panañejo ) - (panañejo * pandeayer) 
descuento = float(descuento)
descuento = round(descuento,2)
descuento = str(descuento)
compradepanañejo = panañejo * pandeayer
compradepanañejo = float(compradepanañejo)
compradepanañejo= round(compradepanañejo,2)
costetotal = compradepanañejo 
costetotal = str(costetotal)
print("el valor del pan de hoy es de 3.49 € por no ser el pan de hoy se desconto " + descuento +" y el valor total es de "+ costetotal + "")
 
