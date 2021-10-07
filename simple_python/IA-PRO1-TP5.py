from random import *
archivo = open("Preguntas.csv","r")
resultado = archivo.readlines()
con = 0
rc = 0
ri = 0
print ("-Juego de preguntas-\n")
while rc < 5 and ri < 3:
    random = randint(0,86)
    for x in resultado:
        x = x.replace("\n","")
        x = x.split(";")
        con = con + 1
        if random == con: p = x
    print (f"{p[0]}\n\n1){p[1]}\n2){p[2]}\n3){p[3]}\n4){p[4]}")
    r = input("Ingrese la respuesta correcta: ")
    respuesta = p[5]
    if respuesta == r:
        rc = rc + 1
        print (f"\nCorrecto, sus respuestas correctas son: {rc}\n")
        print ("".center(45,"-"))
    else:
        ri = ri +1
        print (f"\nIncorrecto, sus respuestas incorrectas son: {ri}\n")
        print ("".center(45,"-"))
    if rc == 5: print ("Usted gano el juego\n:)")
    elif ri == 3: print ("Usted perdio el juego\n:(")
    con = 0