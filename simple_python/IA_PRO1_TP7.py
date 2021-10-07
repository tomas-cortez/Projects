def MostrarSueldos(): 
    archivo = open("IEFI.csv","r")
    datos = archivo.readlines()
    print ("Apellido".ljust(11),"Nombre".ljust(11),"S.Bas".ljust(7),"S.1°Aum".ljust(9),"S.2°Aum","\n")
    for x in datos:
        x = x.replace("\n","")
        x = x.split(";")
        a1 = ( (int(x[5]))+( (int(x[5])*(15/100) )) )
        a2 = ( (int(a1))+( (int(a1)*(12/100) )) )
        print (f"{x[1].ljust(9)}   {x[2].ljust(9)}   {x[5]}   {a1}   {a2}")
    archivo.close()
    
def ExportarSueldos(): 
    archivo = open("IEFI.csv","r")
    datos = archivo.readlines()
    archivo2 = open("IEFI2.csv","w")
    for x in datos:
        x = x.replace("\n","")
        x = x.split(";")
        aa = round( (int(x[4]))*((int(x[5])*(1.7/100)) ),1)
        t = (int(x[5])+aa)
        archivo2.write(x[1]+", "+x[2]+";"+str(x[5])+";"+str(aa)+";"+str(t)+"\n")
    archivo.close()
    archivo2.close()
    
def CalcularPromedio(promedio):
    archivo = open("IEFI.csv","r")
    datos = archivo.readlines()
    c = 0
    s = 0
    for x in datos:
        x = x.replace("\n","")
        x = x.split(";")
        s = s + int(x[5])
        c = c + 1
    promedio = s/c
    print (f"El promedio es: {promedio}")
    return (promedio)
    archivo.close()
    
def ConsultarUnAumentoDeSueldo(legajo):
    archivo = open("IEFI.csv","r")
    datos = archivo.readlines()
    for x in datos:
        x = x.replace("\n","")
        x = x.split(";")
        an = (x[1]+", "+x[2])
        sb = x[5]
        sa = ( (int(x[5]))+( (int(x[5])*(15/100) )) )
        if legajo == int(x[0]): return (print (f"{an} {sb} {sa}"))
        else: return (print ("El legajo es inexistente\n"))
    archivo.close()
 
print ("En este programa puedes hacer las siguientes operaciones:\n",
"1 – Listar los sueldos. \n",
"2 – Exportar los sueldos.\n",
"3 – Calcular el promedio de los sueldos básicos.\n",
"4 – Consultar el aumento de sueldo de un empleado.")

a = int(input("Ingresa el número que corresponde a tu elección: "))
while a < 5:
    if a == 1:
        MostrarSueldos()
    elif a == 2:
        ExportarSueldos()
        print ("Archivo generado exitosamente!")
    elif a == 3:
        CalcularPromedio(a)
    elif a == 4:
        a = int(input ("Legajo: "))
        ConsultarUnAumentoDeSueldo(a)
    print ("En este programa puedes hacer las siguientes operaciones:\n",
    "1 – Listar los sueldos. \n",
    "2 – Exportar los sueldos.\n",
    "3 – Calcular el promedio de los sueldos básicos.\n",
    "4 – Consultar el aumento de sueldo de un empleado.")

    a = int(input("Ingresa el número que corresponde a tu elección: "))
else: (print ("Esa opción no está disponible"))   
print("Fin del programa.")      