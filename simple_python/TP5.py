
from random import randint 

def Procedimiento_1 ():
    a = int(randint(1,6))
    b = int(randint(1,6))

    print ("Se arrojan los dados...")
    print (f"Álvaro saco {a}")
    print (f"Bárbara saco {b}")

    if a > b: print ("El ganador es Álvaro.")
    elif a < b: print ("La ganadora es Bárbara.")
    elif a == b: print ("Ambos obtuvieron el mismo numero, es un empate.")
    
def Procedimiento_2 ():
    
    a = int(randint(1,6))
    a_ = int(randint(1,6))
    b = int(randint(1,6))
    b_ = int(randint(1,6))
    aa = a + a_
    bb = b + b_
    print ("SE ARROJAN LOS DADOS...")
    print (f"Carmen saco {aa}")
    print (f"David saco {bb}")
  
    if aa > bb: print ("La ganadora es Carmen")
    elif aa < bb: print ("El ganador es David")
    elif a > b and a > b_ or a_ > b and a_ > b_:
        print ("Empate, pero Carmen obtuvo el dado con el valor mas alto, por lo tanto, gana.")
        print (f"Los resultados de Carmen fueron: {a,a_} Y los de David: {b,b_}.")
    elif b > a and b > a_ or b_ > a and b_ > a_: 
        print ("Empate, pero David obtuvo el dado con el valor mas alto, por lo tanto, gana.")
        print (f"Los resultados de David fueron: {b,b_} Y los de Carmen: {a,a_}.")
    elif aa == bb and a >= b or a >= b_ or b >= a or b >= a_: print ("Es un empate!")
    elif aa == bb and a_ >= b or a_ >= b_ or b_ >= a or b_ >= a_: print ("Es un empate!")
    
def Procedimiento_3 ():
    a = int(randint(1,3))
    b = int(randint(1,3))
    
    print ("Piedra = (1) || Papel = (2) || Tijera = (3)")
    print (f"Inés {a}")
    print (f"Juan {b}")
    
    if a == 1 and b == 3: print ("Inés obtuvo Piedra y Juan Tijera, la ganadora es Inés")
    elif a == 3 and b == 2: print (f"Inés obtuvo Tijera y Juan Papel, la ganadora es Inés")
    elif a == 2 and b == 1: print (f"Inés obtuvo Papel y Juan Piedra, la ganadora es Inés")
    elif b == 1 and a == 3: print ("Juan obtuvo Piedra e Inés Tijera, el ganador es Juan")
    elif b == 3 and a == 2: print (f"Juan obtuvo Tijera e Inés Papel, el ganador es Juan")
    elif b == 2 and a == 1: print (f"Juan obtuvo Papel e Inés Piedra, el ganador es Juan")
    else: print ("Es un empate")
 
def Procedimiento_4 ():
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese otro numero: "))

    if a > b: print (a)
    elif b > a: print (b)
    elif a == b: print ("Los numeros son iguales.")

def Procedimiento_5 ():

    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese otro numero: "))
    c = float(input("Ingrese otro numero: "))

    if a > b and a > c: print (a)
    elif b > a and b > c: print (b)
    elif c > a and c > b: print (c)
    elif a == b and b != c: print ("Dos de los numeros son iguales")
    elif a == c and a != b: print ("Dos de los numeros son iguales")
    elif b == c and c != a: print ("Dos de los numeros son iguales")
    elif a == b and a == c: print ("Los numeros son iguales.")

def Procedimiento_6 ():
    
    caracter = str(input("Ingrese un caracter: "))
    caracter = (caracter.lower())
    if caracter == "a": print ("El caracter ingresado es una vocal.")
    elif caracter == "e": print ("El caracter ingresado es una vocal.")
    elif caracter == "i": print ("El caracter ingresado es una vocal.")
    elif caracter == "o": print ("El caracter ingresado es una vocal.")
    elif caracter == "u": print ("El caracter ingresado es una vocal.")
    else: print ("El caracter ingresado NO es una vocal.")

def Procedimiento_7 ():
    a = int(0)
    while a <= 100:
        print (a)
        a = a + 1
        
def Procedimiento_8 ():
    for a in range(101):
        print (a)

def Procedimiento_9 ():
    a = (input("Ingrese una palabra: "))
    b = len(a)
    print (f"La palabra tiene {b} letras.") 

def Procedimiento_10 (): 
    for a_ in "Palabra":
        print (a_)    
    
    
    a = str(input("Ingrese una palabra: "))
    for b in (a):
        print (f"Dame una {b}") 
    
    print (a)

def Procedimiento_11 (): 
    a = [12,6,2]
    print (a[0]+a[1]+a[2]) 

def Procedimiento_12 (): 
    a = [1,5,3]
    print (a[0]*a[1]*a[2]) 
    
def Procedimiento_13 (): 
    a = int(input("Ingrese un numero entero: "))
    print (a * "*")
    
def Procedimiento_14 (): 
    a = int(input("Ingrese un numero entero: "))
    b = input("Ingrese un caracter: ")
    print (a * b)
    
def Procedimiento_15 (): 
    a = [19,17,15,13,11,9,7,5,3,1]
    for b in a:
        print (b*"*")

print ("|###################################################################|")
print ("| |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |13| |14| |15| |")
print ("|Para salir ingrese ------------------------------------------>|16| |")
print ("|###################################################################|")
a = int(input("INGRESE EL N° DE OPCIÓN: "))

while a != 16:
    if a == 1:
        Procedimiento_1()
    elif a == 2:
        Procedimiento_2()
    elif a == 3:
        Procedimiento_3()
    elif a == 4:
        Procedimiento_4()
    elif a == 5:
        Procedimiento_5()
    elif a == 6:
        Procedimiento_6()
    elif a == 7:
        Procedimiento_7()
    elif a == 8:
        Procedimiento_8()
    elif a == 9:
        Procedimiento_9()
    elif a == 10:
        Procedimiento_10()
    elif a == 11:
        Procedimiento_11()
    elif a == 12:
        Procedimiento_12()
    elif a == 13:
        Procedimiento_13()
    elif a == 14:
        Procedimiento_14()
    elif a == 15:
        Procedimiento_15()
    else:
        print("No tengo esa opción")
    print ("")
    print ("|###################################################################|")
    print ("| |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |13| |14| |15| |")
    print ("|Para salir ingrese ------------------------------------------>|16| |")
    print ("|###################################################################|")
    a = int(input("INGRESE EL N° DE OPCIÓN: "))
    
print("Fin del programa.") 