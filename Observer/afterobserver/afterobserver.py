from kpi_data import KPI_Data

for kpi in KPI_Data:
	if kpi.nombre == 'abierto':
		print("Tickets abiertos actualmente: {0}".format(kpi.valor))
	elif kpi.nombre == 'nuevo':
		print("Nuevos tickets en la ultima hora: {0}".format(kpi.valor))
	elif kpi.nombre == 'cerrado':
		print("Tickets cerrados en la ultima hora: {0}".format(kpi.valor))