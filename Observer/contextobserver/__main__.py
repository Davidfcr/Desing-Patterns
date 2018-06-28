from kpis import KPIs
from kpis_actuales import KPIs_Actuales
from kpis_pronostico import KPIs_Pronostico

#Reporte de KPI actuales
with KPIs() as kpis:
	with KPIs_Actuales(kpis), KPIs_Pronostico(kpis):
		kpis.set_kpis(25, 10, 5)
		kpis.set_kpis(100, 50, 30)
		kpis.set_kpis(50, 10, 20)

print('\n**** Saliendo del manejador de contextos ****\n\n')
kpis.set_kpis(150, 110, 120)
