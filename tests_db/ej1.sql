/*1.	Determine en una sola consulta el art�culo (c�digo, nombre e importe) que gener� m�s ventas mayoristas 
en el a�o 2006 que el art�culo A205221022 en el 2005. 
Excluya siempre las ventas anuladas. */
USE Ventas2

SELECT 
	Art.articulo as 'C�digo',Art.nombre AS 'Nombre', (MD.precioventa* MD.cantidad) as 'Importe'

FROM mayorcab as MC
	INNER JOIN mayordet as MD ON MC.factura = MD.factura AND MC.letra = MD.letra
	INNER JOIN articulos as Art ON MD.articulo = Art.articulo

WHERE 
	(MD.precioventa* MD.cantidad) > 280
	AND YEAR(MC.fecha) = 2006
	AND mc.anulada = 0

ORDER BY
	importe DESC


/*
2.	Determinar los 10 mejores clientes mayoristas, usando el ranking de compras mostrando aquellos que compraron mas de 1000 prendas 
(cantidad en maydet) y gastaron mas de 50000 pesos (total en maycab) en el segundo semestre de 2005. 
Excluir las ventas anuladas y tomar solamente los clientes activos (estado = 'A') ordenar decreciente por el total vendido. 
*/

SELECT 
	TOP 10
	C.cliente
	,C.nombre
	,SUM(MD.cantidad) as cantidad
	,SUM(MC.total) as total

FROM
	clientes C 
	INNER JOIN mayorcab MC on MC.cliente = c.cliente
	INNER JOIN mayordet MD on (MC.letra = MD.letra and MC.factura = MD.factura)
WHERE
	MC.fecha between '2005-06-01' and '2005-12-31'
	AND c.estado = 'A'
	AND mc.anulada = 0
GROUP BY 
	C.cliente
	,C.nombre
HAVING
	SUM(MD.cantidad) > 1000 and SUM(MC.total) > 50000
ORDER BY
	SUM(MC.total) desc




