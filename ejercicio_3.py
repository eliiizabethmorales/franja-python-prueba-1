#  Escribir un programa que haga transformaciones de pesos a dólares. 
# Debe preguntarle al usuario si desea transformar de pesos mexicanos a dólares,
#  de pesos chilenos a dólares, o desde pesos argentinos a dólares.
#  Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares

#solucion:
numero = int(input(''' hola si desea cambiar de:
pesos mexicanos a dolares escriba 1
pesos chilenos a dolares escriba 2
pesos argentinos a dolares escriba 3'''))
pesos = input("ahora ingrese cuantos pesos desea cambiar:")
pesos = float(pesos)
if numero == 1:
    valor_dolarmex = 20
    dolaresmex = pesos / valor_dolarmex
    dolaresmex= float(dolaresmex)
    dolaresmex = round(dolaresmex, 2)
    dolaresmex = str(dolaresmex)
    print("usted cambio de pesos mexicanos a dolares entonces tiene " +dolaresmex+" dolares ")
elif numero == 2:
    valor_dolarclp = 855
    dolaresclp = pesos / valor_dolarclp
    dolaresclp= float(dolaresclp)
    dolaresclp = round(dolaresclp, 2)
    dolaresclp = str(dolaresclp)
    print("usted cambio de pesos chilenos a dolares entonces tiene "+dolaresclp+" dolares")
else:
    valor_dolararg = 115
    dolaresarg = pesos / valor_dolararg
    dolaresarg =float(dolaresarg)
    dolaresarg = round(dolaresarg,2)
    dolaresarg = str(dolaresarg)
    print("usted cambui de pesos argentinos a dolares entonces tiene "+dolaresarg+" dolares")