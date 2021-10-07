#1
def suma():
    a = int(input("Ingrese el primer Numero: "))
    b = int(input("Ingrese el segundo Numero: ")) 
    c = (a + b)
    print (c)
#2           
def resta():
    print ("Ingrese dos numeros diferentes")
    a = int(input("Ingrese el primer Numero: "))
    b = int(input("Ingrese el segundo Numero: "))
    
    if a != b and a > b: print (a-b)
    elif a != b and a < b: print (b-a)
    elif a == b: print ("Los numeros son iguales, el resultado es 0 ")
#3        
def producto():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print (f"El resultado del producto de {a} y {b} es: {a*b}")
#4
def max():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    
    if a > b: print (f"El mayor de los numeros es: {a}")
    elif b > a: print (f"El mayor de los numeros es: {b}")
    elif a == b: print (f"{a} y {b} son iguales")
#5    
def min():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    
    if a < b: print (f"El menor de los numeros es: {a}")
    elif b < a: print (f"El menor de los numeros es: {b}")
    elif a == b: print (f"{a} y {b} son iguales")
#6
def max_de_tres():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))
    
    if a > b and a > c: print (f"El mayor de los numeros es: {a}")
    elif b > a and b > c: print (f"El mayor de los numeros es: {b}")
    elif c > a and c > b: print (f"El mayor de los numeros es: {c}")
    elif a == b and a == c: print ("Los numeors son iguales")
#7    
def vocal():
    a = str(input("Ingrese un caracter: "))
    b = a.lower()
    
    if b == "a" or b == "e" or b == "i" or b == "o" or b == "u": print (True)
    else: print (False)
#8
def inversa():
    a = input("Ingrese lo que quiera invertir: ")
    print (a[::-1])
#9    
def es_palindromo():
    a = input("Ingrese una palabra: ")
    b = (a[::-1])
    
    if a == b: print ("Es palindromo")
    elif a != b: print ("No es palindromo")

#10
def len_cadena():
    a = str(input("Ingrese una cadena de caracteres: "))
    contador = 0
    
    for i in a:
        contador += 1
        
    print (f"La longitud de la cadena es de ||{contador}|| caracteres.")
      
#11
def superposicion():
    a = str(input("Ingrese una cadena de caracteres: "))
    b = str(input("Ingrese otra cadena de caracteres: "))
    c = 0
    
    for i in a:
        for I in b:
            if i == I: c += 1
    if c > 0: print (True)
    elif c <= 0:  print (False)

#12
def generar_n_caracteres():
    a = int(input("Ingrese un Numero entero: "))
    b = str(input("Ingrese un Caracter: "))
    print (a*b)

    
    
    
    
    
    
    
    
    
    
    