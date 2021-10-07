
import json
from neo4j import GraphDatabase

grafodb=GraphDatabase.driver(uri='bolt://localhost:7687',auth=('neo4j','miguel'))
sesion=grafodb.session()

with open('paises_100.json') as archivo:
	filas = json.load(archivo)
	for fila in filas:
		q1 = "CREATE (:Pais {nombre: '" + fila['country'] + "'})"
		sesion.run(q1)

q1 = "MATCH(n:Pais) WHERE n.nombre='China' RETURN COUNT(n) AS can"
nodos = sesion.run(q1)
for nodo in nodos:
	print(nodo)


	