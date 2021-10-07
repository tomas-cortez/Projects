# -*- coding: utf-8 -*-
"""
Base de Datos
Cortez Tomás.
"""

import pyodbc
import pandas as pd 
from funpymodeling.data_prep import todf
from sklearn.linear_model import LinearRegression
import numpy as np

"""-------------------------------------------------------------------------"""
server = 'DESKTOP-V38GL8V\SQLEXPRESS'
database = 'Ventas2' 
username = 'sa' 
password = 'admin' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM estimaciones;')

estimaciones = cursor.fetchall()
df=todf(estimaciones)
df=pd.DataFrame(df)
df.rename(columns={0:'Articulo',1:'Año',2:'Ventas'},inplace=True)
cursor.close()
cnxn.close()
""" ----------------------------------------------------------------------------"""
x=df[['Año']]
y=df[['Ventas']]
nuevo_x = np.array([2009]) 
regresion_lineal = LinearRegression()
regresion_lineal.fit(x,y)
prediccion = regresion_lineal.predict(nuevo_x.reshape(-1,1))
"""------------------------------------------------------------------------------"""

articulo = input("INGRESE EL CODIGO DEL ARTICULO: ")

if articulo == 'A102270075':
    print("=================")
    print(df.to_csv(columns=['Año', 'Ventas'],sep='\t', index=False))
    print("=================")
    print("ESTIMADO 2009:",int(prediccion))

else: print('Codigo Incorrecto, reinicie el programa')







