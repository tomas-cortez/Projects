
def Empleados1(): 
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    print ("Nombre:".ljust(20," "),"Categoria:".ljust(24," "),"Basico".ljust(8," "),
           "Antig.".ljust(9," "),"Pres.".ljust(9," "),"Total")
    for x in datos:
        x = x.replace("\n", "")
        x = x.split(";")
        anti = ((int(x[6]))*(int(x[5]))*(1.2/100))
        pre = ((int(x[6])+anti)*(8.35/100))
        total = (round(pre+anti+int(x[6]),2))
        print (x[1].ljust(20," "),x[2].ljust(24," "),x[6].ljust(8," "),
               round(anti,1),"  ",round(pre,1),"  ",total,)
    archivo.close()
        
def Empleados2():
    a = int(input("Ingrse el año de antigüedad: "))
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    for x in datos:
        x = x.replace("\n", "")
        x = x.split(";")
        if int(x[5]) > a: print (x[1].ljust(20),x[2].ljust(20),x[6])
    archivo.close()

def Empleados3():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    archivo2 = open("DatosPrograma2.csv","w")
    for x in datos:
        x = x.replace("\n", "")
        col = x.split(";")
        anti = ((int(col[6]))*(int(col[5]))*1.2/100)
        pre = ((int(col[6])+anti)*(8.35/100))
        total = (round(pre+anti+int(col[6]),2))
        archivo2.write(col[1]+";"+col[2]+";"+col[6]+";"+str(anti)+";"
                       +str(pre)+";"+str(total)+";"+"\n")
    archivo.close()

def Empleados4():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    archivo2 = open("DatosPrograma3.csv","w")
    a = input("Ingrese el nombre de la categoria: ").lower()
    for x in datos:
        x = x.replace("\n", "")
        x = x.split(";")
        if x[2].lower() == a: archivo2.write(str(x[1])+";"+str(x[2])+";"+str(x[6])+";"+"\n")
    archivo.close()   

def Empleados5():
    a = int(input("Ingrse el año de antigüedad: "))
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    archivo2 = open("DatosPrograma4.csv","w")
    for x in datos:
        x = x.replace("\n", "")
        x = x.split(";")
        if int(x[5]) > a: archivo2.write(str(x[1])+";"+str(x[2])+";"+x[6]+";"+"\n")
    archivo.close() 

def Empleados6():
    a = int(input("Ingrse el N° de lagajo: "))
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    print ("Nombre:".ljust(13," "),"Cat.:".ljust(9," "),"Bas.".ljust(6," "),
           "Antig.".ljust(4," "),"Pres.".ljust(6," "),"Total")
    for x in datos:
        x = x.replace("\n", "")
        x = x.split(";")
        anti = ((int(x[6]))*(int(x[5]))*(1.2/100))
        pre = ((int(x[6])+anti)*(8.35/100))
        total = (round(pre+anti+int(x[6]),2))
        if int(x[0]) == a:
            print(x[1].ljust(12),x[2].ljust(10),x[6].ljust(6),round(anti,1),round(pre,1),total)
    archivo.close()   

def Empleados7():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    total = 0
    for x in datos:
        x = x.split(";")
        c = int(x[6])
        total = total+c
    print (f"Total de los sueldos basicos: {total}")
    archivo.close()   

def Empleados8():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    total = 0
    cp = 0
    for x in datos:
        x = x.split(";")
        c = int(x[6])
        cp = cp+1
        total = total+c
    total = total/cp
    print (total)
    print (f"Total de promedio de los sueldos basicos es: {int(total/cp)}")
    archivo.close()   

def Empleados9():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    mayor = 0
    for x in datos:
        x = x.split(";")
        d = int(x[6])
        if d > mayor:
            mayor = d
            f = x[1]
    print (f"{f} | total= {mayor}")
    archivo.close()   

def Empleados10():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    suma = 0
    for x in datos:
        x = x.split(";")
        anti = ((int(x[6]))*(int(x[5]))*1.2/100)
        suma = suma + anti
    print (f"El total a pagar es: {suma}")
    archivo.close()  

def Empleados11():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    suma = 0
    pro = 0
    c = 0
    for x in datos:
        x = x.split(";")
        pro = pro + 1
        c += 1
        anti = ((int(x[6]))*(int(x[5]))*1.2/100)
        suma = suma + anti
    pro = suma/c
    print (f"El promedio a pagar es: {round(pro,2)}")
    archivo.close()  
    
def Empleados12():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    suma = 0
    for x in datos:
        x = x.split(";")
        anti = ((int(x[6]))*(int(x[5]))*1.2/100)
        pre = ((int(x[6])+anti)*(8.35/100))
        suma = suma + pre
    print (f"El total a pagar es: {round(suma,2)}")
    archivo.close()  

def Empleados13():
    archivo = open("DatosPrograma.csv","r")
    datos = archivo.readlines()
    suma = 0
    pro = 0
    c = 0
    for x in datos:
        x = x.split(";")
        c+=1
        anti = ((int(x[6]))*(int(x[5]))*1.2/100)
        pre = ((int(x[6])+anti)*(8.35/100))
        suma = suma + pre
    pro=suma/c
    print (f"El total a pagar es: {round(pro,2)}")
    archivo.close() 

print ("|#########################################################|")
print ("| |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |12| |13| |")
print ("|Para salir ingrese -------------------------------->|14| |")
print ("|#########################################################|")
a = int(input("INGRESE EL N° DE OPCIÓN: "))
while a != 14:
    if a == 1:
        Empleados1()
    elif a == 2:
        Empleados2()
    elif a == 3:
        Empleados3()
    elif a == 4:
        Empleados4()
    elif a == 5:
        Empleados5()
    elif a == 6:
        Empleados6()
    elif a == 7:
        Empleados7()
    elif a == 8:
        Empleados8()
    elif a == 9:
        Empleados9()
    elif a == 10:
        Empleados10()
    elif a == 11:
        Empleados11()
    elif a == 12:
        Empleados12()
    elif a == 13:
        Empleados13()
    else:
        print("No tengo esa opción")
    print ("")
    print ("|###############################################|")
    print ("| |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| |11| |")
    print ("|Para salir ingrese ---------------------->|11| |")
    print ("|###############################################|")
    a = int(input("INGRESE EL N° DE OPCIÓN: "))
    
print("Fin del programa.")  



        
