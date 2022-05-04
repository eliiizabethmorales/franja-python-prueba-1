# Escribir un programa que le pregunte al usuario una cantidad a invertir,
#  el interés porcentual anual y el número de años,
#  y muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales

#solucion:




inversion = input("hola cual es la cantidad que desea invertir:")
interesanual = input("cual es el interes porcentual anual: ")
cantidaddeaños = input("numero de años:")
inversion=float(inversion)
interesanual= float(interesanual)
cantidaddeaños= float(cantidaddeaños)
capitalfinal = (inversion * ((( interesanual / 100 ) + 1)) ** cantidaddeaños)
capitalfinal =int(capitalfinal)
capitalfinal= float(capitalfinal)
capitalfinal = round(capitalfinal,2)
capitalfinal = str(capitalfinal)
print("el capital final obtenido en la inversion es : "+ capitalfinal + "")