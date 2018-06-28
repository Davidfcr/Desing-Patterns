from observer import AbsObserver

class KPIs_Actuales(AbsObserver):
	_tickets_abiertos = -1
	_tickets_cerrados = -1
	_tickets_nuevos = -1

	def __init__(self, kpis):
	    self._kpis = kpis
	    kpis.attach(self)
		
	def update(self):
		self.tickets_abiertos = self._kpis.tickets_abiertos
		self.tickets_cerrados = self._kpis.tickets_cerrados
		self.tickets_nuevos = self._kpis.tickets_nuevos
		self.mostrar_info()

	def mostrar_info(self):
		print("Tickets abiertos actualmente: {0}".format(self.tickets_abiertos))
		print("Nuevos tickets en la ultima hora: {0}".format(self.tickets_nuevos))
		print("Tickets cerrados en la ultima hora: {0}".format(self.tickets_cerrados))
		print('*******\n')
