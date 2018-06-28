from kpis import KPIs
from kpis_actuales import KPIs_Actuales
from kpis_pronostico import KPIs_Pronostico

#Reporte de KPI actuales
kpis = KPIs()
kpis_actuales = KPIs_Actuales(kpis)
kpis_pronostico = KPIs_Pronostico(kpis)
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)

print('\n**** Desacoplando el observador KPIs_Actuales ****\n\n')
kpis.detach(kpis_actuales)
kpis.set_kpis(150, 110, 120)
