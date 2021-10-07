from tp3 import *

print ("|####################################################|")
print ("| |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |")
print ("|Para salir ingrese --------------------------->|13| |")
print ("|####################################################|")
a = int(input("INGRESE EL N° DE OPCIÓN: "))

while a != 13:
    if a == 1:
        suma()
    elif a == 2:
        resta()
    elif a == 3:
        producto()
    elif a == 4:
        max()
    elif a == 5:
        min()
    elif a == 6:
        max_de_tres()
    elif a == 7:
        vocal()
    elif a == 8:
        inversa()
    elif a == 9:
        es_palindromo()
    elif a == 10:
        len_cadena()
    elif a == 11:
        superposicion()
    elif a == 12:
        generar_n_caracteres()
    else:
        print("No tengo esa opción")
    print ("")
    print ("|####################################################|")
    print ("| |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |")
    print ("|Para salir ingrese --------------------------->|13| |")
    print ("|####################################################|")
    a = int(input("INGRESE EL N° DE OPCIÓN: "))
    
print("Fin del programa.") 