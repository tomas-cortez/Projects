/*
EJERCICIO 1

El artículo B107130014 es una Campera de Cuero clásica de alto valor, de la cual, cuando la empresa comenzó su actividad
se distribuyeron 3 unidades de cada talle en cada sucursal para su venta. Se precisa determinar el stock actual de ese artículo
en cada sucursal, siempre y cuando sea mayor a cero. Listar el nombre de la sucursal, el talle, la cantidad vendida y la cantidad
actual, ordenado por sucursal y talle.
*/
USE Ventas2
SELECT
	S.denominacion AS "Sucursal"
	,VD.talle AS "Talle"
	,SUM(VD.cantidad) AS "Stock Vendido"
	,15 - SUM(VD.cantidad) AS "Stock Actual"
FROM 
	Vencab AS VC 
	INNER JOIN Vendet VD ON (VC.letra= VD.letra AND VC.factura = VD.factura)
	INNER JOIN Sucursales S ON VC.sucursal = S.sucursal
WHERE 
	VD.articulo = 'B107130014'
	AND VC.anulada = 0
GROUP BY
	S.denominacion
	,VD.talle
HAVING
    15 - SUM(VD.cantidad) > 0
ORDER BY
	1, 2

/*
EJERCICIO 2

Cree la vista v_comisiones_vendedores_2008, donde se calculen las comisiones que le corresponden a cada vendedor
para cada mes del año 2008, de acuerdo a sus ventas, su antigüedad y su categoría.
El criterio de cálculo de las comisiones es el siguiente: 
- Si el vendedor es encargado, la comisión mensual es del 0.05, y se le pagan $500 adicionales por cada año de antigüedad.
- Si el vendedor NO es encargado, la comisión mensual es de 0.03 y se le pagan $300 adicionales por cada año de antigüedad.
Listar el código del vendedor, el nombre, si es o no encargado, la antigüedad, el mes (vencab), el importe total de ventas 
y la comisión a cobrar. Tenga en cuenta:
- Utilice como referencia para el cálculo de la antigüedad el año de ingreso del vendedor y el año en el que la empresa hizo su última venta.
- Excluya ventas anuladas.
- Solamente se deben pagar comisiones si el vendedor superó los $5000 en ventas en cada mes.
*/

CREATE OR ALTER VIEW v_comisiones_vendedores_2008 AS
-- Encargados
SELECT
	vc.vendedor AS Vendedor,
	v.nombre AS Nombre,
	v.encargado AS Encargado,
	2009 - YEAR(v.ingreso) AS Antigüedad,
	MONTH(vc.fecha) AS Mes,
	SUM(vc.total) AS Total,
	(SUM(vc.total) * 0.05) + (2009 - YEAR(v.ingreso)) * 500 AS Comisión
FROM
	vencab as vc
	INNER JOIN vendedores AS v
	ON vc.vendedor = v.vendedor
WHERE
	YEAR(vc.fecha) = 2008
	AND vc.anulada = 0
	AND v.encargado = 'S'
GROUP BY
	vc.vendedor,
	v.nombre,
	v.encargado,
	2009 - YEAR(v.ingreso),
	MONTH(vc.fecha)
HAVING
	SUM(vc.total) > 5000
--
UNION
-- No encargados
SELECT
	vc.vendedor AS Vendedor,
	v.nombre AS Nombre,
	v.encargado AS Encargado,
	2009 - YEAR(v.ingreso) AS Antigüedad,
	MONTH(vc.fecha) AS Mes,
	SUM(vc.total) AS Total,
	(SUM(vc.total) * 0.03) + (2009 - YEAR(v.ingreso)) * 300 AS Comisión
FROM
	vencab as vc
	INNER JOIN vendedores AS v
	ON vc.vendedor = v.vendedor
WHERE
	YEAR(vc.fecha) = 2008
	AND vc.anulada = 0
	AND v.encargado = 'N'
GROUP BY
	vc.vendedor,
	v.nombre,
	v.encargado,
	2009 - YEAR(v.ingreso),
	MONTH(vc.fecha)
HAVING
	SUM(vc.total) > 5000

-- Verificación

SELECT * FROM v_comisiones_vendedores_2008 ORDER BY Vendedor, Mes

/*
EJERCICIO 3

Cree la tabla TmpArticulosSinVentas, que contenga los artículos que no registraron nunca una venta,
ni mayorista ni minorista. La estructura de la tabla debe ser código, nombre, marca (nombre),
rubro (nombre), preciomayor y preciomenor. Resuelva en una sola instrucción. 
*/


SELECT
	a.articulo AS Articulo,
	a.nombre AS Nombre,
	m.nombre AS Marca,
	r.nombre AS Rubro,
	a.preciomayor AS PrecioMayor,
	a.preciomenor AS PrecioMenor
INTO
	TmpArticulosSinVentas
FROM
	articulos AS a
	INNER JOIN rubros AS r
	ON a.rubro = r.rubro
	INNER JOIN marcas AS m
	ON a.marca = m.marca
WHERE
	a.articulo NOT IN (SELECT DISTINCT articulo FROM vendet) AND
	a.articulo NOT IN (SELECT DISTINCT articulo FROM mayordet)
ORDER BY
	1

SELECT * FROM TmpArticulosSinVentas

DROP TABLE TmpArticulosSinVentas