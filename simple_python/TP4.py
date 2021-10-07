def ContarCaracter():
    a = input("Ingrese una frase: ")
    b = input("Ingrese un caracter: ")
    c = 0
#Si se quiere usar en minuscula uso: "x = x.lower()" 
    for i in a:
        if i == b: c += 1      
    print (f"El caracter se encuentra {c} veces en la frase.")


def CalcularSumatoria():
    a = int(input("Ingrese un numero entero entre 0 y 10: "))
    b = 0
    if a >= 0 and a <= 10:
        for i in range(a+1): b = i + b
        print (f"La suma de los valores es {b}")
    else: print ("El numero es invalido")     
       
    
def ConsultarPrecio():
    a = int(input("Ingrese su edad: "))
    
    if a >= 0 and a <= 130:
        if a < 4: print ("El valor de la entrada es de $25")
        elif a >= 4 and a < 18: print ("El valor de la entrada es de $75")
        elif a >= 18: print ("El valor de la entrada es de $100")
    else: print ("La edad es icorrecta")


def CalificarAlumno():
    a = int(input("Ingrese un numero entero comprendido entre 0 y 10: "))
    if a >= 1 and a <= 10:
        if a >= 1 and a <= 3: print ("No satifactorio")
        elif a == 4: print ("Suficiente")
        elif a >= 5 and a <= 6: print ("Satifactorio")
        elif a == 7: print ("Bueno")
        elif a >= 8 and a <= 9: print ("Muy bueno")
        elif a == 10: print ("Exelente")
    else: print ("El numero es invalido.")

print("------------------------------------------------------------------------")
print ("En este programa puedes hacer las siguientes operaciones:")
print ("")
print ("1 – Conocer cuántos caracteres de un tipo tiene un texto.")
print ("2 - Conocer la sumatoria de 0 hasta un número ingresado por el usuario.")
print ("3 - Conocer el precio de una entrada.")
print ("4 - Conocer cuál es la calificación cualitativa de un alumno.")
print ("5 - Salir del programa")
print ("")
print("------------------------------------------------------------------------")

a = int(input("Ingresa el número que corresponde a tu elección: "))        

while a != 5:
    if a == 1:
        ContarCaracter()
    elif a == 2:
        CalcularSumatoria()
    elif a == 3:
        ConsultarPrecio()
    elif a == 4:
        CalificarAlumno()
    else: print ("No tengo esa opcion")
    print("------------------------------------------------------------------------")
    print ("En este programa puedes hacer las siguientes operaciones:")
    print ("")
    print ("1 – Conocer cuántos caracteres de un tipo tiene un texto.")
    print ("2 - Conocer la sumatoria de 0 hasta un número ingresado por el usuario.")
    print ("3 - Conocer el precio de una entrada.")
    print ("4 - Conocer cuál es la calificación cualitativa de un alumno.")
    print ("5 - Salir del programa")
    print ("")
    print("------------------------------------------------------------------------")

    a = int(input("Ingresa el número que corresponde a tu elección: ")) 

print ("Fin del programa.")