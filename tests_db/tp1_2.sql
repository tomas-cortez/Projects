use ventas2
select vd.articulo as "Articulo",
	YEAR(vc.fecha) as "Año"
	,SUM(vd.cantidad) as "Ventas"
INTO estimaciones 
from
	vencab as vc
	inner join vendet as vd
	on vd.factura = vc.factura and vd.letra = vc.letra

where
	vc.anulada=0
	and vd.articulo = 'A102270075'
group by
	YEAR(vc.fecha),vd.articulo

SELECT * FROM estimaciones;